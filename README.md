# 🚀 Tips Hindawi Internship (August–October) 2026

🎓 This project was built during the Tips Hindawi Internship (August–October) 2026.

---

## 👤 Participant

| Field | Value |
|---|---|
| Full Name | Nada Ibrahim Issa Muhammed |
| Project Name | Research Paper RAG Agent |
| GitHub Username | nada2essa |
| Internship Batch | August–October 2026 |
| Training Program | Large Language Models (LLMs) Program |
| Organization | Edrak for Ai |

---

## 📖 Project Overview

This project is an AI-powered Research Paper Assistant based on Retrieval-Augmented Generation (RAG).

The application allows users to upload one or more PDF research papers. The system extracts the text from the papers, removes reference and bibliography pages, splits the documents into smaller chunks, generates embeddings, and stores them in a local FAISS vector index.

Users can then ask questions about the uploaded research papers or request a summary of a paper.

For research-related questions, the system retrieves the most relevant passages from the uploaded papers and generates a grounded answer with citations and the retrieved source passages.

If the requested information cannot be answered from the uploaded papers, the assistant automatically falls back to general knowledge.

---

## ✨ Features

- 📄 Upload one or more PDF research papers.
- 🔎 Extract and process text from uploaded documents.
- 🧹 Remove reference/bibliography pages.
- ✂️ Split documents into smaller chunks.
- 🧠 Generate embeddings for document chunks.
- 🗃️ Store embeddings in a local FAISS vector database.
- 🔍 Retrieve the most relevant passages for each question.
- 🤖 Generate grounded answers using retrieved research content.
- 📚 Provide citations and display retrieved source passages.
- 📝 Summarize research papers.
- 🧭 Automatically route requests between:
  - RAG Agent
  - Summarizer
  - General Knowledge Agent
- 🌐 Answer general knowledge questions when the uploaded papers do not contain the required information.

---

## 🛠️ Technologies Used

- Python
- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
- LangChain
- FAISS
- Embeddings
- Natural Language Processing (NLP)
- Semantic Search
- PDF Text Extraction
- Generative AI
- AI Agents / Query Routing

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/nada2essa/research-assistant-rag.git
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file and add the required API keys and configuration values used by the project.

### 5. Run the application

Run the project's main application file according to the project structure.

For example:

```bash
streamlit run app.py
```

Replace the command above with the actual entry point of the project if your application uses a different file.

---

## 🚀 Usage

### 1. Upload Research Papers

Upload one or more PDF research papers from the sidebar.

### 2. Document Processing

The application automatically:

1. Extracts text from the PDFs.
2. Removes reference/bibliography pages.
3. Splits the text into chunks.
4. Generates embeddings.
5. Stores the embeddings in a local FAISS index.

### 3. Ask Questions

Enter a question in the chat input.

The router determines whether the request is:

- A research question
- A summarization request
- A general knowledge question

### 4. Research Questions

For questions related to the uploaded papers, the system retrieves the most relevant chunks and generates a grounded response with citations.

Example:

```text
What is self-attention?
Explain the Transformer architecture.
What methodology is proposed?
What are the experimental results?
```

### 5. Summarization

You can ask the assistant to summarize a research paper.

Example:

```text
Summarize the paper.
```

### 6. General Knowledge

If the answer cannot be found in the uploaded papers, the assistant automatically falls back to general knowledge.

Example:

```text
What is Python?
Explain Machine Learning.
What is Artificial Intelligence?
What is the difference between CNN and RNN?
```

---

## 📸 Demo

### Uploading a Research Paper

### RAG Agent

### Summarizer

### General Agent

### Interface

---

## 📈 Results

The project provides an interactive research assistant capable of:

- Processing multiple research papers.
- Performing semantic search over uploaded documents.
- Retrieving relevant research passages.
- Generating answers grounded in the uploaded papers.
- Providing citations and source passages.
- Summarizing research papers.
- Automatically handling questions outside the uploaded documents using general knowledge.

The project demonstrates the practical application of RAG, embeddings, vector databases, LLMs, and intelligent query routing in a real-world document intelligence application.

---

## 💡 Example Questions

### Research Questions

- What is self-attention?
- Explain the Transformer architecture.
- What methodology is proposed?
- Summarize the paper.
- What are the experimental results?

### General Knowledge Questions

- What is Python?
- Explain Machine Learning.
- What is Artificial Intelligence?
- What is the difference between CNN and RNN?

---

## 🔮 Future Improvements

- [ ] Conversation memory across turns
- [ ] Chat history export
- [ ] Hybrid search (BM25 + FAISS)
- [ ] OCR support for scanned PDFs
- [ ] Image and table understanding
- [ ] Multi-language support
- [ ] PDF highlighting for cited passages
- [ ] Streaming LLM responses
- [ ] Clickable citation hyperlinks
- [ ] Docker deployment

---

## 📚 About the Internship

This project was developed as part of the Tips Hindawi Internship (August–October) 2026, and it will be showcased on the official Tips Hindawi website.

Tips Hindawi is the internships department of Edrak for Ai. The internship encourages participants to build real-world projects, apply practical skills, and showcase their work through GitHub.

For more information about the internship, training programs, and upcoming batches, visit the official Tips Hindawi website.

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a Pull Request.

---

## 📄 License

This project is shared for educational and portfolio purposes.

---

## 👨‍💻 Author

**Nada Ibrahim Issa Muhammed**

GitHub: [nada2essa](https://github.com/nada2essa)

### Areas of Interest

- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
- LangChain & AI Orchestration
- Machine Learning
- Natural Language Processing (NLP)
- Generative AI
- Semantic Search
- Vector Databases (FAISS)
- Data Science & Analytics
- MLOps & Model Deployment
- Conversational AI & Intelligent Agents
- Document Intelligence

---

⭐️ If you found this project useful, consider giving it a star on GitHub.
