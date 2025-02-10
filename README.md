# A LLM-based chatbot as Q&A system for Vietnamese higher education environment
## Author
- Bui Quang Thien
- Nguyen Thi Phu
## Overview
Chatbots have become crucial in everyday modern life. It is not until large language models began their era that people interact with chatbox on screen for informative answers. Nonetheless, the rises of Artificial Intelligence provide numerous solutions for advanced improvements, enabling clients to take advantage of smarter, human-like systems. On the other side, such agents may not deliver ideal or even appropriate data in some specific contexts. This paper introduces a chatbot that were built to be fit in Vietnamese university society. We focus on designing a system that combines open-source language model and Retrieval-Augmented Generation (RAG) approach for higer conversasion quality. Furthermore, Deep Q-Learning, a reinforcement learning method, is preferred to keep the consistency over time at a low cost.
## Method
The method combines modern natural language processing (NLP) techniques with advanced data querying tools to assist in answering students' questions quickly and accurately.
### 1. Data source processing 
The source data is extracted from an accessible Vietnamese PDF file. The content from the PDF file is preprocessed and converted into a raw text file, ensuring that only information related to students is retained
The Frequently Asked Questions (FAQ) system is designed to address common student inquiries. The FAQ data is stored in a PostgreSQL database with the following structure: 
    • ques_embed: precomputed vector embeddings of frequently asked questions
    • ques: the text of frequently asked questions
    • ans: the corresponding answers.
### 2. Query & RAG processing 
When a user enters a question, the system converts it into a vector embedding using BGE to ensure compatibility between the user's question and the stored data. The system compares the question vector with those in the FAQ using Cosine Similarity. Once the similarity score reaches or exceeds the 73% threshold

The seven most relevant text passages from ChromaDB based on the user's question. The retrieved passages, along with the user's question, are sent to a quantized version of Google’s Gemma 2 9B LLM, which then processes the input to synthesize and generate an appropriate response. The system is deployed using LlamaCPP, an open-source library optimized for running LLMs on standard computing devices. The 73% similarity threshold was chosen based on practical testing to balance accuracy and the ability to identify complex questions requiring the RAG process. 
![image](https://github.com/user-attachments/assets/00d8af71-7eda-4343-9775-f70d39df563c)
### 3. Reinforcement Learning for response optimization 
To improve the accuracy and relevance of responses in the FAQ system, we apply reinforcement learning based on user feedback. Users can interact with the chatbot by marking responses with a like or dislike, providing valuable data for optimizing future answers.

![image](https://github.com/user-attachments/assets/6695d0be-686d-41e5-85ef-36bc353e22e5)

![image](https://github.com/user-attachments/assets/266cd64e-ab4f-4b57-9fb7-25504920f73c)


