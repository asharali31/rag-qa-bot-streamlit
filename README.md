# 📚 RAG QA Bot (Streamlit)

A simple Retrieval‑Augmented Generation (RAG) question‑answering bot built with Streamlit, LangChain, Chroma, and Groq.

## ✨ Features

- 📄 **Upload a PDF document**
- ✂️ **Extract text and split into chunks**
- 🧠 **Generate embeddings using HuggingFace sentence‑transformers**
- 💾 **Store vectors in a local Chroma database**
- ❓ **Answer questions about the document using a RetrievalQA chain powered by Groq's Llama‑3.1‑8B‑instant model**
- 🖥️ **Clean, minimal Streamlit UI**

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/asharali31/rag-qa-bot-streamlit.git
   cd rag-qa-bot-streamlit
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your Groq API key:
   - Copy `env_template.txt` to `.env`
   - Edit `.env` and replace `your_groq_api_key_here` with your actual Groq API key.

## ▶️ Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

1. Open the browser tab that opens (usually http://localhost:8501).
2. Upload a PDF file using the file uploader.
3. After the document is processed, type a question about the document in the text input and click **Get Answer**.
4. The answer will appear below.

## 📁 Project Structure

- `app.py` – Main Streamlit application
- `rag_utility.py` – Functions for processing PDFs, creating embeddings, and answering queries
- `requirements.txt` – Python dependencies
- `env_template.txt` – Template for environment variables (Groq API key)
- `chroma_db/` – Directory where the vector store is persisted (created at runtime)

## 📦 Dependencies

See `requirements.txt` for the full list. Key packages:
- `streamlit`
- `langchain` and related components (`langchain-community`, `langchain-huggingface`, `langchain-chroma`, `langchain-groq`)
- `unstructured` (for PDF loading)
- `sentence-transformers`
- `python-dotenv`

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [LangChain](https://www.langchain.com/)
- Vector storage via [Chroma](https://www.trychroma.com/)
- LLM inference provided by [Groq](https://groq.com/)
- Embedding models from [HuggingFace](https://huggingface.co/)
