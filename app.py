import streamlit as st
import requests

# ------------------------------
# Configuration
# ------------------------------
OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3:latest"

# ------------------------------
# Streamlit Page Setup
# ------------------------------
st.set_page_config(
    page_title="Local LLM Chat (Ollama)",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Local LLM Chat Interface")
st.caption("Powered by Ollama + Streamlit")

# ------------------------------
# Session State (Conversation History)
# ------------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ------------------------------
# Reset Button
# ------------------------------
if st.button("🔄 Reset Conversation"):
    st.session_state.chat_history = []
    st.experimental_rerun()

# ------------------------------
# Display Conversation History
# ------------------------------
st.subheader("💬 Conversation")

for role, message in st.session_state.chat_history:
    if role == "user":
        st.markdown(f"**🧑 You:** {message}")
    else:
        st.markdown(f"**🤖 Model:** {message}")

# ------------------------------
# User Input
# ------------------------------
user_input = st.text_input("Ask something:", placeholder="Type your question here...")

# ------------------------------
# Send Query to Ollama
# ------------------------------
if st.button("Send") and user_input.strip():

    # Add user message to history
    st.session_state.chat_history.append(("user", user_input))

    # Build full conversation context
    full_prompt = ""
    for role, msg in st.session_state.chat_history:
        if role == "user":
            full_prompt += f"User: {msg}\n"
        else:
            full_prompt += f"Assistant: {msg}\n"

    payload = {
        "model": MODEL_NAME,
        "prompt": full_prompt,
        "stream": False
    }

    try:
        response = requests.post(
            OLLAMA_API_URL,
            json=payload,
            timeout=120
        )
        response.raise_for_status()
        model_reply = response.json().get("response", "No response received.")
    except Exception as e:
        model_reply = f"Error: {e}"

    # Add model response to history
    st.session_state.chat_history.append(("assistant", model_reply))

    # Refresh UI
    st.experimental_rerun()
