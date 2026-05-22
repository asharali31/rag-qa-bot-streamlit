import os
from dotenv import load_dotenv

from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_classic.chains import RetrievalQA 

# load the env variables from .env file
load_dotenv()

# get the current working directory
working_dir = os.path.dirname(os.path.abspath(__file__))

# load the embedding model
embedding = HuggingFaceEmbeddings() 

# load the llm model from groq
llm = ChatGroq(
    model = "llama-3.1-8b-instant",
    temperature=0.0
)

def process_document_to_chroma_db(file_name):
    # load the pdf document using UnstructuredPDFLoader
    loader = UnstructuredPDFLoader(f"{working_dir}/{file_name}")
    documents = loader.load()
    
    # split the document text into smaller chunks for embedding
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 2000,
        chunk_overlap = 200
    )
    text_chunks = text_splitter.split_documents(documents)

    # store the document chunks in chroma vector database
    vectordb = Chroma.from_documents(
        documents = text_chunks,
        embedding = embedding,
        persist_directory = f"{working_dir}/chroma_db"
    )
    return vectordb

def get_answer_from_user_query(user_query):
    # load the persistent chroma vector database
    vectordb = Chroma(
        embedding_function = embedding,
        persist_directory = f"{working_dir}/chroma_db"
    )

    # create a retriever for document search
    retriever = vectordb.as_retriever()

    # create a RetrievalQA chain to answer user query using llm
    qa_chain = RetrievalQA.from_chain_type(
        llm = llm,
        chain_type = "stuff",
        retriever = retriever
    )

    response = qa_chain.invoke({"query": user_query})
    answer = response["result"]
    return answer
