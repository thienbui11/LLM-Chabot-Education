﻿# A LLM-based chatbot as Q&A system for Vietnamese higher education environment
## Author
- Bui Quang Thien
- Nguyen Thi Phu
  
## Demo
FAQ responses

![image](https://github.com/user-attachments/assets/66750412-2b33-4500-8163-0d5c2806ff6a)

![image](https://github.com/user-attachments/assets/c03e6b25-71e4-4167-ba50-574e67acb640)

RAG responses

![image](https://github.com/user-attachments/assets/4c273b1f-4eb2-431e-a06c-62e6bbd535a2)

![image](https://github.com/user-attachments/assets/d5313db3-f8bc-44a4-8123-a845ae543dc0)

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

To optimize answer selection, we implement a reinforcement learning environment using the Deep Q-Learning algorithm. The environment is deployed in the DQLEnv class, where each state is represented as a vector embedding created by concatenating the question embedding with the embeddings of the two candidate answers. The action space consists of two choices: selecting the first or second answer.

![image](https://github.com/user-attachments/assets/2e11390a-d37e-4fb8-8f9e-b6ab43685694)

The reward function reflects user satisfaction, calculated as a logarithmic function of the ratio of likes to total interactions, with a time-decay factor to prioritize long-term valuable responses. This logarithmic function prevents excessive reward fluctuations across episodes, ensuring stable learning dynamics.

![image](https://github.com/user-attachments/assets/73688d7e-3dba-4ff7-8aad-1694946dcc06)


The environment operates by initializing the state through a reset function, which includes the question embedding and two responses. When an action is performed, the step function returns a reward based on user feedback stored in the Feedback table, maintaining the initial state for continuous evaluation. This design enables the chatbot to progressively learn and prioritize the most relevant responses to user inquiries.

## Experiments And Results

To evaluate the effectiveness of the chatbot in supporting consultation on training rules and regulations, the team conducted a series of experiments. These experiments aimed to test the chatbot's ability to retrieve information and generate feedback based on the Retrieval Augmented Generation (RAG) method. 

The experiments were conducted with a Tesla P100-PCIE-16GB GPU, featuring 16GB of VRAM, which is sufficient for optimizing the model layers. 

### 1. Datasets

We made use of a student handbook formally named “Sổ tay sinh viên 2023” as one of the data sources. The document was published and made accessible by the Admissions and Student Affairs Office of Ho Chi Minh city University of Technologies and Educationi. There are entirely 141 pages from the handbook. By reserving only raw texts, our database got approximately 10 pages. 

As no question was provided, the remaining data was compiled from the school’s community Q&A serviceii. The site is managed by a group of verified advisors, which makes it another reliable source. Questions are split into faculties as sections. ... The number of collected questions is approximately 100, distributed among faculties as follows:

    • Faculty of Information Technology: 27% (~27 questions)
    • Faculty of Mechanical Engineering: 22% (~22 questions)
    • Faculty of Electrical and Electronics Engineering: 20% (~20 questions)
    • Faculty of Civil Engineering: 17% (~17 questions)
    • Other Faculties: 14% (~14 questions)
    
### 2. Experimental results

![image](https://github.com/user-attachments/assets/583537e7-8483-432b-a7bb-6d3a1ddaf76f)

## Conclusion

This project presented the development of an LLM-based chatbot designed specifically for the Vietnamese higher education environment. By integrating an open-source language model with the Retrieval-Augmented Generation (RAG) approach, the system ensures more accurate and contextually relevant responses to students' inquiries. Additionally, a Frequently Asked Questions (FAQ) module is implemented to enhance response efficiency for common queries. The incorporation of Deep Q-Learning into the chatbot offers a significant advantage by allowing the system to self-improve over time, ensuring that it adapts to the evolving needs of students and the university community. By continuously optimizing its response strategy based on user interactions, the chatbot maintains a high level of relevance and accuracy in its answers. This approach not only enhances the user experience but also ensures that the system remains efficient and scalable, even as the volume of users and queries increases.

Although there are limitations in data scope, contextual understanding, and response time, the team has gained valuable lessons and established a foundation for future improvements. With plans to enhance accuracy, contextual analysis capabilities, and comprehensive data integration, the chatbot is expected to become a highly effective tool, contributing to the modernization of management and improving the learning experience for students.

## References
    [1] Georgia State University, "Pounce Chatbot," an automated assistant supporting students with enrollment and financial aid inquiries.  https://mainstay.com/case-study/how-georgia-state-university-supports-every-student-with-personalized-text-messaging/ 
    [2] Deakin University, "Genie," a digital assistant offering 24/7 support for academic and administrative queries. 
    [3] Interacting with educational chatbots: A systematic review https://link.springer.com/article/10.1007/s10639-022-11177-3
    [4] “Sổ tay sinh viên 2023”, HCMC University of Technology And Education. https://sao.hcmute.edu.vn/ArticleId/e8db4387-3f43-4770-a67c-90fa85ce009f/so-tay-sinh-vien-2023
    [5] School’s community Q&A service, HCMC University of Technology And Education. https://tuvansinhvien.hcmute.edu.vn/ 
    [6] Cheonsu Jeong. 2024. A Study on the Implementation Method of an Agent-Based Advanced RAG System Using Graph.   https://arxiv.org/pdf/2407.19994 
    [7] Samina Amin, Deep Q-Learning(DQN) https://medium.com/@samina.amin/deep-q-learning-dqn-71c109586bae 
    [8] Mandar Kulkarni, Praveen Tangarajan, Kyung Kim, Anusua Trivedi. 2024. Reinforcement Learning for Optimizing RAG for Domain Chatbots https://arxiv.org/pdf/2401.06800 
    [9] Yunfan Gaoa , Yun Xiongb , Xinyu Gaob , Kangxiang Jiab , Jinliu Panb , Yuxi Bic , Yi Daia , Jiawei Suna , Meng Wangc , and Haofen Wang. 2024. Retrieval-Augmented Generation for Large Language Models: A Survey https://arxiv.org/pdf/2312.10997 
    [10] Tobias Abdon, Creating a Streaming Chat Application with Django & OpenAI: A Step-By-Step Guide https://discovergen.ai/article/creating-a-streaming-chat-application-with-django/ 
    [11] Zackary Rackauckas, RAG-FUSION: A NEW TAKE ON RETRIEVAL-AUGMENTED GENERATION https://arxiv.org/pdf/2402.03367 

