import os
import re
import time
import shutil
import streamlit as st


from retriever import get_retriever
from agents import (
    answer_question,
    general_answer,
    summarize_document
)
from router import route_question
from create_vector_db import create_vector_db


def get_full_document_text():

    from langchain_community.document_loaders import PyPDFLoader

    text = ""

    if os.path.exists("data"):

        for file in os.listdir("data"):

            if file.endswith(".pdf"):

                loader = PyPDFLoader(
                    os.path.join("data", file)
                )

                pages = loader.load()

                for page in pages:
                    text += page.page_content + "\n\n"

    return text

def show_general_answer(question):

    with st.chat_message("assistant"):

        status = st.empty()
        status.info("🤔 Thinking...")

        start = time.time()

        answer = general_answer(question)

        elapsed = time.time() - start

        status.empty()

        st.success("🌍 General Knowledge")

        placeholder = st.empty()

        text = ""

        for word in answer.split():
            text += word + " "
            placeholder.markdown(text + "▌")
            time.sleep(0.008)  # 0.005–0.01 gives a smooth effect

        placeholder.markdown(text)

        st.caption(f"⏱ Response Time: {elapsed:.2f} sec")

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

# ---------------- Page ----------------

st.set_page_config(
    page_title="Multi-Agent Research Assistant",
    page_icon="📚",
    layout="centered"
)
# ---------------- Session ----------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "retriever" not in st.session_state:
    try:
        st.session_state.retriever = get_retriever()
    except:
        st.session_state.retriever = None

# ---------------- Sidebar ----------------

with st.sidebar:

    st.title("📚 Research Assistant")

    st.markdown("---")

    st.subheader("📂 Upload Research Papers")

    uploaded_files = st.file_uploader(
        "Drag & Drop PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:

        os.makedirs("data", exist_ok=True)

        for file in uploaded_files:
            with open(
                    os.path.join("data", file.name),
                    "wb"
            ) as f:
                f.write(file.getbuffer())

        with st.spinner("Creating Vector Database..."):

            create_vector_db("data")

        st.session_state.retriever = get_retriever()

        st.success("✅ Vector Database Ready")

    st.markdown("---")

    if st.button("🗑 Clear Uploaded PDFs", use_container_width=True):

        # Delete uploaded PDFs
        if os.path.exists("data"):

            for file in os.listdir("data"):

                if file.endswith(".pdf"):
                    os.remove(os.path.join("data", file))

        # Delete FAISS vector database
        if os.path.exists("vectorstore"):
            shutil.rmtree("vectorstore")

        # Reset retriever
        st.session_state.retriever = None

        st.success("✅ Uploaded PDFs and Vector Database cleared.")

    st.markdown("---")

    st.subheader("Features")

    st.write("✅ Multi-Agent Routing")
    st.write("✅ RAG")
    st.write("✅ General Knowledge")
    st.write("✅ FAISS Vector Search")
    st.write("✅ Citations")

    st.markdown("---")

    if st.button("🗑 Clear Chat"):

        st.session_state.messages = []

        st.rerun()

# ---------------- Main ----------------

st.title("📚 Multi-Agent Research Assistant")

st.caption(
    "Ask questions from research papers or general knowledge."
)

# Show chat history

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# Chat input

question = st.chat_input(
    "Ask a general question, ask about the uploaded paper, or type 'summarize'"
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    route = route_question(question)


    # ---------------- SUMMARY ----------------

    if route == "SUMMARY":

        if (
                not os.path.exists("data")
                or not any(
            file.endswith(".pdf")
            for file in os.listdir("data")
        )
        ):
            st.error("Please upload PDF files first.")
            st.stop()

        with st.chat_message("assistant"):

            status = st.empty()
            status.info("📄 Summarizing document...")

            start = time.time()

            full_text = get_full_document_text()

            answer = summarize_document(full_text)

            elapsed = time.time() - start

            status.empty()

            st.success("📑 Document Summary")

            st.markdown(answer)

            st.caption(f"⏱ Response Time: {elapsed:.2f} sec")

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

    # ---------------- QUESTION (RAG or GENERAL) ----------------

    else:

        retriever = st.session_state.retriever

        # No PDF uploaded → General Knowledge

        if retriever is None:
            show_general_answer(question)

            st.stop()

        # Similarity search

        results = retriever.similarity_search_with_score(
            question,
            k=3
        )

        # Lower score = more relevant

        best_score = results[0][1]

        THRESHOLD = 1.2

        # Unrelated → General Knowledge

        if best_score > THRESHOLD:
            show_general_answer(question)

            st.stop()


      # Relevant → use RAG

        docs = [doc for doc, score in results]

        if not docs:

            st.error("No relevant documents found.")

            st.stop()

        context = ""

        references = []

        reference_map = {}

        source_number = 1

        for doc in docs:

            text = re.sub(
                r"\[\d+(?:,\s*\d+)*\]",
                "",
                doc.page_content
            )

            filename = os.path.basename(
                doc.metadata.get("source", "Unknown")
            )

            page = doc.metadata.get("page", 0) + 1

            key = (filename, page)

            if key not in reference_map:

                reference_map[key] = source_number

                references.append(
                    (source_number, filename, page)
                )

                source_number += 1

            number = reference_map[key]

            context += f"""
    [Source {number}]
    {text}
    
    """

        with st.chat_message("assistant"):

            status = st.empty()
            status.info("📄 Searching research papers...")

            start = time.time()

            answer = answer_question(question, context)

            elapsed = time.time() - start

            status.empty()

            st.success("📄 Retrieval-Augmented Generation")

            placeholder = st.empty()

            text = ""

            for word in answer.split():
                text += word + " "
                placeholder.markdown(text + "▌")
                time.sleep(0.008)  # 0.005–0.01 gives a smooth effect

            placeholder.markdown(text)

            used = sorted(
                set(
                    int(x)
                    for x in re.findall(
                        r"\[(\d+)\]",
                        answer
                    )
                )
            )

            if used:

                st.markdown("### 📚 References")

                for number, filename, page in references:

                    if number in used:

                        st.write(
                            f"**[{number}]** {filename} — Page {page}"
                        )

            with st.expander("📄 Retrieved Documents"):

                for i, doc in enumerate(docs, 1):

                    filename = os.path.basename(
                        doc.metadata.get(
                            "source",
                            "Unknown"
                        )
                    )

                    page = doc.metadata.get(
                        "page",
                        0
                    ) + 1

                    st.markdown(
                        f"**📄 {filename} (Page {page})**"
                    )

                    st.write(doc.page_content)

                    st.divider()

            st.caption(
                f"⏱ Response Time: {elapsed:.2f} sec"
            )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )