import streamlit as st 
import os 
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import faiss
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain 
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from langchain_ollama import OllamaEmbeddings, ChatOllama
import warnings 
warnings.filterwarnings("ignore", category=DeprecationWarning) 

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")
    return vector_store

def get_conversation_chain():
    prompt_template = """Answer the question from the provided context, make sure to provide all the details which matches exactly with the document, if the answer is not in the context just don't provide answer and just say 'I don't know but can find similar solution sources over the internet to help' and if the user say they want the solution provide links that matches with the specific description of the document file which is available on the internet and answer the solution based on the knowledge the document and internet has about the question.
    Context: \n{context}\n
    Question: \n{question}\n
    
    Answer:
    """
    models = "llama3.2"
    llm = ChatOllama(model=models,temperature=0.3) 
    
    prompt = PromptTemplate(
        template=prompt_template,
        input_variables={"context": None, "question": None}
    )
    
    chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt)
    return chain

def user_input(user_question):
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    new_db = FAISS.load_local("faiss_index",embeddings,allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)
    
    chain = get_conversation_chain()
    
    response = chain.invoke({"input_documents": docs, "question": user_question})
    st.write(response["output_text"])
def main():
    load_dotenv()
    st.set_page_config(page_title="PDFAnswers ", page_icon="📄")
    st.title("PDFAnswers ")
    st.header("Chat with PDFs :books:")
    
    user_question = st.text_input("Ask a question about your PDFs")
    if user_question:
        user_input(user_question)
    
    
    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Upload your PDFs", accept_multiple_files=True)
        
        if st.button("Process"):
            with st.spinner("Processing..."):
                # Get PDF text
                raw_text = get_pdf_text(pdf_docs)
                # Get the text chunks
                text_chunks = get_text_chunks(raw_text)
                st.write(text_chunks)
                # Create vector store
                get_vector_store(text_chunks) 
                st.success("Done!")      

if __name__ == "__main__":
    main()
