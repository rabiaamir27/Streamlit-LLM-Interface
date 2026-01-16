Local LLM Chat Interface using Streamlit & Ollama

This project implements a simple and interactive web-based chat interface using Streamlit that connects to a locally hosted Large Language Model (LLM) running via Ollama. The application allows users to ask questions, receive AI-generated responses, view conversation history, and reset the chat — all without relying on cloud-based APIs.

Features:
Interactive web UI built with Streamlit
Connects to a local LLM via Ollama
Text input for user queries
Real-time AI-generated responses
Conversation history panel
Reset conversation functionality
Fully offline inference after model download

Technologies Used:
Python 3
Streamlit
Ollama
LLaMA 3 (llama3:latest)
REST API (HTTP)

System Architecture
User (Browser)
      ↓
Streamlit Web Interface
      ↓  (HTTP POST Request)
Ollama Local API (localhost:11434)
      ↓
LLaMA 3 Model (Local Inference)

Prerequisites
Python 3.8 or later
Ollama installed and running
At least one Ollama model downloaded (e.g. llama3)
Installation & Setup
Install Python Dependencies
python -m pip install streamlit requests

Install and Run Ollama
Download Ollama from:
https://ollama.com

Pull and run the model:
ollama run llama3

Ensure Ollama is running at:
http://localhost:11434

Run the Streamlit app:
python -m streamlit run app.py

Open your browser at:
http://localhost:8501

Usage:
Enter a question in the text input box
Click Send to get a response from the local LLM
View previous messages in the conversation panel
Click Reset Conversation to clear chat history

Project Structure:
.
├── app.py          # Streamlit application
├── README.md       # Project documentation

Key Highlights:
No internet required after model download
No external API keys
Privacy-friendly (runs entirely on local machine)
Suitable for learning, experimentation, and academic projects


