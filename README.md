# Corrective RAG Chatbot

A production-oriented **Corrective Retrieval-Augmented Generation (CRAG)** chatbot built with **LangGraph, LangChain, Gemini, FAISS, Tavily, and Streamlit**.

The system evaluates retrieved documents before generating an answer. If the retrieved context is irrelevant or insufficient, it automatically rewrites the query and performs a web search to improve the final response.

---

## Features

- **Corrective RAG Pipeline**
  - Evaluates retrieved documents for relevance before generation.
  - Classifies retrieval quality as `CORRECT`, `INCORRECT`, or `AMBIGUOUS`.

- **Adaptive Retrieval**
  - Uses FAISS for semantic document retrieval.
  - Keeps relevant documents based on LLM-based evaluation.

- **Query Rewriting**
  - Automatically transforms the original question into an optimized web-search query when local retrieval is insufficient.

- **Web Search Fallback**
  - Uses Tavily to retrieve external information when the local knowledge base cannot adequately answer the question.

- **Context Refinement**
  - Splits retrieved content into sentences.
  - Filters irrelevant sentences before passing context to the generation model.

- **Gemini LLM**
  - Uses Google's Gemini model for document evaluation, query rewriting, context filtering, and answer generation.

- **Gemini Embeddings**
  - Uses Gemini embeddings to convert documents into vector representations for semantic search.

- **FAISS Vector Store**
  - Performs efficient similarity-based document retrieval.

- **LangGraph Workflow**
  - Implements the complete RAG workflow as a stateful graph with conditional routing.

- **Streamlit Interface**
  - Provides an interactive chat interface for querying the RAG system.

---


## Tech Stack

| Technology    | Purpose                         |
| ------------- | ------------------------------- |
| Python        | Core programming language       |
| LangChain     | LLM and RAG components          |
| LangGraph     | Stateful workflow orchestration |
| Google Gemini | LLM and embeddings              |
| FAISS         | Vector similarity search        |
| Tavily        | Web search fallback             |
| Streamlit     | Web-based chatbot interface     |
| PyPDF         | PDF document processing         |
| Pydantic      | Structured LLM outputs          |
| python-dotenv | Environment variable management |

---

## Architecture

```text
                         User Question
                              │
                              ▼
                    ┌──────────────────┐
                    │  FAISS Retriever │
                    └────────┬─────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Document Evaluation │
                  │      Gemini         │
                  └─────────┬───────────┘
                            │
                 ┌──────────┼──────────┐
                 │          │          │
              CORRECT   AMBIGUOUS   INCORRECT
                 │          │          │
                 │          └────┬─────┘
                 │               │
                 │               ▼
                 │       ┌────────────────┐
                 │       │ Query Rewriting│
                 │       │     Gemini     │
                 │       └───────┬────────┘
                 │               │
                 │               ▼
                 │       ┌────────────────┐
                 │       │ Tavily Search  │
                 │       └───────┬────────┘
                 │               │
                 └───────┬───────┘
                         │
                         ▼
                ┌──────────────────┐
                │ Context Refining │
                │     Gemini       │
                └────────┬─────────┘
                         │
                         ▼
                 ┌───────────────┐
                 │ Answer        │
                 │ Generation    │
                 │ Gemini        │
                 └───────┬───────┘
                         │
                         ▼
                    Final Answer
