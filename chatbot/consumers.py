import json
import uuid
import requests
from django.template.loader import render_to_string 
from channels.generic.websocket import WebsocketConsumer
from django.conf import settings

FLASK_APP_ENDPOINT = "https://zep.hcmute.fit/7889/generate"

def _format_token(token: str) -> str:
     # apply very basic formatting while we're rendering tokens in real-time
     token = token.replace("\n", "<br>")
     return token

class ChatConsumerDemo(WebsocketConsumer):
    def connect(self):
        self.user = self.scope["user"]
        self.messages = []
        if self.user.is_authenticated:
            self.accept()
        else:
            self.close()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_text = text_data_json["message"]

        # do nothing with empty messages
        if not message_text.strip():
            return

        # add to messages
        self.messages.append(
            {
                "role": "user",
                "content": message_text,
            }
        )

        # show user's message
        user_message_html = render_to_string(
            "chatbot/user_message_demo.html",
            {
                "message_text": message_text,
            },
        )
        self.send(text_data=user_message_html)

        # render an empty system message where we'll stream our response
        message_id = uuid.uuid4().hex
        contents_div_id = f"message-response-{message_id}"
        system_message_html = render_to_string(
            "chatbot/system_message.html",
            {
                "contents_div_id": contents_div_id,
            },
        )
        self.send(text_data=system_message_html)
        
        # call chatgpt api
        # client = OpenAI(api_key=settings.OPENAI_API_KEY)
        # openai_response = client.chat.completions.create(
        #     model=settings.OPENAI_MODEL,
        #     messages=self.messages,
        #     stream=True,
        # )
        data = {
            "prompt": self.messages,
            "stream": True 
        }
        response = requests.post(FLASK_APP_ENDPOINT, json=data, stream=True)
        chunks = []
        for chunk in response:
            message_chunk = chunk.choices[0].delta.content
            if message_chunk:
                chunks.append(message_chunk)
                # use htmx to insert the next token at the end of our system message.
                chunk = f'<div hx-swap-oob="beforeend:#{contents_div_id}">{_format_token(message_chunk)}</div>'
                self.send(text_data=chunk)

        system_message = "".join(chunks)
        # replace final input with fully rendered version, so we can render markdown, etc.
        final_message_html = render_to_string(
            "chatbot/final_system_message_demo.html",
            {
                "contents_div_id": contents_div_id,
                "message": system_message,
            },
        )
        # add to messages
        self.messages.append(
            {
                "role": "system",
                "content": system_message,
            }
        )
        self.send(text_data=final_message_html)