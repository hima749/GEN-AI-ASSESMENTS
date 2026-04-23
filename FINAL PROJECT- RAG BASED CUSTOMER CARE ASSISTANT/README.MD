# 📌 Retrieval-Augmented Generation (RAG) System using LangGraph

## 🚀 Overview
This project implements a **Retrieval-Augmented Generation (RAG)** system that answers user queries based on a given document.  
It combines **information retrieval** with **language generation** to provide accurate and context-aware responses.

---

## 🎯 Objective
The goal of this project is to:
- Reduce hallucination in AI-generated responses  
- Provide **document-based answers**  
- Build a modular workflow using **LangGraph**

---

## 🧠 How It Works

The system follows these steps:

1. **Document Loading**
   - Loads a PDF document using PyPDFLoader  

2. **Chunking**
   - Splits document into smaller chunks for better processing  

3. **Embedding**
   - Converts text into vector embeddings using HuggingFace model  

4. **Vector Storage**
   - Stores embeddings in ChromaDB  

5. **Retrieval**
   - Retrieves most relevant chunks based on user query  

6. **Answer Generation**
   - Uses GPT-2 model to generate answer based on retrieved context  

7. **LangGraph Integration**
   - Structures workflow into nodes for scalability and modularity  

---

## 🛠️ Technologies Used

- Python  
- LangChain  
- LangGraph  
- ChromaDB  
- HuggingFace Embeddings  
- GPT-2 (Transformers)  
- Google Colab  

---

## 📂 Project Structure

