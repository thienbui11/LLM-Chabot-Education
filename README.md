# A LLM-based chatbot as Q&A system for Vietnamese higher education environment
## Author
- Bui Quang Thien
- Nguyen Thi Phu
- 
## Demo
FAQ responses

![image](https://github.com/user-attachments/assets/66750412-2b33-4500-8163-0d5c2806ff6a)

![image](https://github.com/user-attachments/assets/c03e6b25-71e4-4167-ba50-574e67acb640)

RAG responses

![image](https://github.com/user-attachments/assets/4c273b1f-4eb2-431e-a06c-62e6bbd535a2)

![image](https://github.com/user-attachments/assets/d5313db3-f8bc-44a4-8123-a845ae543dc0)

## Overview
Chatbots have become crucial in everyday modern life. It is not until large language models began their era that people interact with chat box on screen for informative answers. Nonetheless, the rises of artificial intelligence provide numerous solutions for advanced improvements, enabling clients to take advantage of smarter, human-like systems. On the other side, such agents may not deliver ideal or even appropriate data in some specific contexts, particularly when dealing with nuanced local information. This paper introduces a chatbot that were built to be fit in Vietnamese university societies. We focus on designing a system that combines open-source language model and Retrieval-Augmented Generation (RAG) approach for higher conversation quality with limited real-world Q&A dataset. Furthermore, DeepnQ-Learning, a reinforcement learning method, is applied to keep thenconsistency over time at an acceptable cost. Our multiple experimentsnshow promising results, indicating the potential for highly effective adoption within Vietnam institutions.

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

![image](https://github.com/user-attachments/assets/948efa6f-04c9-4a24-ad18-66ce02ef96fa)

![image](https://github.com/user-attachments/assets/d692da89-3401-4029-beaf-94f7035348fb)

![image](https://github.com/user-attachments/assets/d2605647-82df-4108-9ce2-60abf96ad51a)

## Conclusion

This paper presents the development of an LLM-based chatbot designed specifically for the Vietnamese higher education environment. By integrating an open-source language model with the Retrieval-Augmented Generation (RAG) approach, the system ensures more accurate and contextually  relevant responses to students' inquiries. Additionally, a Frequently Asked Questions (FAQ) system is implemented to enhance response efficiency for common queries. The incorporation of Deep Q-Learning into the chatbot offers a significant advantage by allowing the system to self-improve over time, ensuring that it adapts to the evolving needs of students and the university community. By continuously optimizing its response strategy based on user interactions, the chatbot maintains a high
level of relevance and accuracy in its answers. This approach not only enhances the user experience but also ensures that the system remains efficient and scalable.

Although there are limitations in hardware and data availability, we have gained valuable lessons and established a foundation for future improvements. With plans to enhance accuracy, contextual analysis capabilities, and comprehensive data integration, the chatbot is expected to become an effective tool, contributing to the modern university and improving the learning experience for students.

## References
    [1] Georgia State University, "Pounce Chatbot," an automated assistant supporting students with enrollment and financial aid inquiries.  https://mainstay.com/case-study/how-georgia-state-university-supports-every-student-with-personalized-text-messaging/ 
    [2] G. Atwell, “Deakin's Genie: a virtual digital assistant out of the bottle”, Deakin University. Accessed: Feb. 10 2025. [Online]. Available: https://www.deakin.edu.au/about-deakin/news-and-media-releases/articles/deakins-genie-a-virtual-digital-assistant-out-of-the-bottle.
    [3] S. Moola, “Benefits of AI in higher education”, REGENT BUSINESS SCHOOL - Higher Education Institution. Accessed: Feb. 10 2025. [Online]. Available: https://regent.ac.za/blog/benefits-of-ai-in-higher-education
    [4] Gao, Yunfan, et al., “Retrieval-Augmented Generation for Large Language Models: A Survey”, arXiv preprint arXiv:2312.10997, 2024
    [5] S. Gupta, R. Ranjan, S. N. Singh, “A Comprehensive Survey of Retrieval-Augmented Generation (RAG): Evolution, Current Landscape and Future Directions”, arXiv preprint arXiv:2410.12837, 2024
    [6] M. Kulkarni, P. Tangarajan, K. Kim, A. Trivedi, “Reinforcement Learning for Optimizing RAG for Domain Chatbots”, arXiv preprint arXiv:2401.06800, 2024
    [7] H. Dong, Z. Ding, and S. Zhang, Deep Reinforcement Learning: Fundamentals, Research and Applications. 1st ed. Singapore: Springer, 2020, p. 123
    [8] Serway, Raymond A.; Moses, Clement J.; Moyer, Curt A, Modern Physics. 3rd ed. Cengage Learning, 2004, p. 481.
    [9] The Office of Admissions and Student Affairs, “Sổ tay sinh viên 2023”, HCMC University of Technology and Education. Accessed: Feb. 12 2025. [Online]. Available: https://sao.hcmute.edu.vn/ArticleId/e8db4387-3f43-4770-a67c-90fa85ce009f/so-tay-sinh-vien-2023 
    [10] University Q&A service, HCMC University of Technology and Education. Accessed: Feb. 15 2025. [Online]. Available: https://tuvansinhvien.hcmute.edu.vn/

