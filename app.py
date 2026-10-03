import streamlit as st
from rag_pipeline import app

st.set_page_config(
    page_title="Corrective RAG",
    layout="centered"
)

st.title("Corrective RAG")
st.caption("Gemini + LangGraph + FAISS + Tavily")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask a question...")

if question:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            result = app.invoke(
                {
                    "question": question,
                    "docs": [],
                    "good_docs": [],
                    "verdict": "",
                    "reason": "",
                    "strips": [],
                    "kept_strips": [],
                    "refined_context": "",
                    "web_query": "",
                    "web_docs": [],
                    "answer": ""
                }
            )

            answer = result["answer"]

        st.markdown(answer)

        with st.expander("RAG Details"):
            st.write("Verdict:", result["verdict"])
            st.write("Reason:", result["reason"])

            if result["web_query"]:
                st.write("Web Query:", result["web_query"])

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )