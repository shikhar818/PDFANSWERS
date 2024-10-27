
# PDFANSWERS
**PDFANSWERS** is an AI-powered interface designed to answer questions from multiple PDF documents by utilizing embeddings, a vector store, and a large language model (LLM). The project employs Retrieval-Augmented Generation (RAG) to improve response accuracy by retrieving relevant document chunks before generating answers.

## Architecture Overview

The architecture comprises the following components:

1. **PDF Reader (Py2PDF)**: 
   - Handles the ingestion of multiple PDFs and splits them into manageable text chunks.
   - Each PDF is processed and split into document chunks with the help of Long Chain Text Splitter.

2. **Embeddings**:
   - Each document chunk is converted into an embedding (vector representation) using models like Llama 3.2 and OpenAI's embeddings.
   - These embeddings are stored in a **Vector Store** (knowledge base) for efficient similarity search.

3. **Vector Store (FAISS)**:
   - A vector storage mechanism, here using FAISS, which enables efficient retrieval of relevant document embeddings based on user queries.
   - The concept of Retrieval-Augmented Generation (RAG) is employed, where the system retrieves relevant chunks from the vector store to use in answering queries.

4. **Semantic Search**:
   - When a user submits a question, the query is embedded and a semantic search is conducted within the vector store to find relevant chunks.
   - The most relevant results are ranked and passed to the LLM for answer generation.

5. **Large Language Model (LLM)**:
   - The ranked results are input to an LLM (e.g., Llama 3.2 or OpenAI) to generate coherent answers based on the retrieved information.

6. **Frontend (Streamlit)**:
   - A user-friendly interface built with Streamlit allows users to interact with the tool, ask questions, and receive answers.

## Workflow


![workflow](https://github.com/user-attachments/assets/c94cb17a-cbff-4b09-bab2-1d3074c9ee13)


1. **Input PDFs**: Multiple PDFs are loaded and split into document chunks.
2. **Embedding Generation**: Each chunk is converted into embeddings.
3. **Vector Store Ingestion**: Embeddings are stored in FAISS for fast retrieval.
4. **User Query**: A user submits a question via the Streamlit frontend.
5. **Question Embedding**: The query is embedded and matched against the vector store.
6. **Semantic Search & Ranking**: Relevant document chunks are retrieved and ranked.
7. **Answer Generation**: The LLM uses the ranked results to generate an answer.
8. **Output**: The generated answer is displayed in the Streamlit interface.

## Output 
1. Find exactly what is present in the document (only if prompt is according to the information present in the document structure)
   
   ![1](https://github.com/user-attachments/assets/2368de4e-66a8-48f9-8a6f-5fbb18247baf)
   ![2](https://github.com/user-attachments/assets/4680a00a-f3bc-402c-b89b-f5ed616f97a5)
   
2. Search for additional information based on the knowledge of LLM and PDFs
   
   ![3](https://github.com/user-attachments/assets/4671627f-5a8a-42af-8660-ac74ed77fccc)
   
3. Defines the process of flowcharts in a research paper(it's not accurate depicition but has some potential to make the user understand some of the concepts)
   
   ![4](https://github.com/user-attachments/assets/53f15240-f80e-497b-9cca-fa12e1135f38)

## Result 
With adequate computational resources, the PDFANSWERS project holds substantial potential to revolutionize information retrieval from digital documents. Designed as a powerful tool for locating specific and diverse information across extensive digital archives, PDFANSWERS would enable users to rapidly access answers to their questions with remarkable accuracy and efficiency.

This application is particularly relevant for fields requiring intensive document analysis, such as research, legal compliance, academia, and corporate intelligence. By integrating advanced AI models for embedding and retrieval, along with a streamlined user interface, PDFANSWERS can dramatically reduce the time spent on manual information extraction. Users can rely on its ability to pinpoint precise answers across numerous PDFs, transforming the way organizations approach data-driven decision-making.

With continual refinement and computational support, PDFANSWERS could redefine the standards of digital document analysis, fostering a more efficient and responsive approach to information management.

## Getting Started

### Prerequisites

- Python 3.9.4
- Streamlit
- FAISS
- OpenAI / Llama API access (for embedding generation and LLM)
- Py2PDF (or any PDF reader library)



