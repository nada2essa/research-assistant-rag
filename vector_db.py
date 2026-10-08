import os
import re

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


def create_vector_db(data_folder):
    documents = []

    # Load all PDFs
    for file in os.listdir(data_folder):

        if file.endswith(".pdf"):

            pdf_path = os.path.join(data_folder, file)

            print(f"Loading: {file}")

            loader = PyPDFLoader(pdf_path)

            pages = loader.load()

            for page in pages:

                text = page.page_content

                # Skip reference/bibliography pages
                if (
                    "References" in text
                    or "REFERENCES" in text
                    or "Bibliography" in text
                    or "BIBLIOGRAPHY" in text
                ):
                    continue

                documents.append(page)

    print(f"\nLoaded {len(documents)} pages.")

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=600,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    # Debug (optional)
    print("\nSample Chunks:")
    for i, chunk in enumerate(chunks[:3]):
        print(f"\n--- Chunk {i + 1} ---")
        print(chunk.page_content[:300])

    # Create embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Create FAISS vector database
    vector_db = FAISS.from_documents(
        chunks,
        embeddings
    )

    # Save locally
    vector_db.save_local("vectorstore")

    print("\n✅ Vector database created successfully!")

    return vector_db


if __name__ == "__main__":
    create_vector_db("data")