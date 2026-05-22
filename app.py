import os
import streamlit as st
from rag_utility import process_document_to_chroma_db, get_answer_from_user_query

# get the current working directory
working_dir = os.path.dirname(os.path.abspath(__file__))

# streamlit page setup
st.set_page_config(
    page_title="RAG QA Bot",
    page_icon="📚",
    layout="centered",
)

st.title("📚 RAG Question Answering Bot")

# file uploader for pdf document
uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])

if uploaded_file is not None:
    # save the uploaded file to the current directory
    save_path = os.path.join(working_dir, uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # process the uploaded document and store in chroma db
    process_document = process_document_to_chroma_db(uploaded_file.name)
    st.success("Document uploaded and processed successfully!")

# user input for question
user_query = st.text_input("Ask a question about the document:")

if st.button("Get Answer"):
    if user_query:
        answer = get_answer_from_user_query(user_query)
        st.markdown(f"**Answer:** {answer}")
    else:
        st.warning("Please enter a question to get an answer.") 
