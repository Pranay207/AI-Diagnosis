import streamlit as st
from openai import OpenAI

# Initialize OpenAI client with your key
client = OpenAI(api_key="sk-...your-api-key-here...")  # Replace with your actual key

# Streamlit page settings
st.set_page_config(page_title="Medical Chatbot", page_icon="💊")
st.title("💊 AI Medical Chatbot")
st.markdown(
    "Ask health-related questions and get helpful insights powered by AI.\n\n"
    "> ⚠️ This is not a substitute for professional medical advice."
)

# Setup chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful medical assistant."}]

# Display previous messages
for msg in st.session_state.messages[1:]:  # Skip system prompt
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Type your medical question here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get response
    with st.chat_message("assistant"):
        with st.spinner("Thinking... 💭"):
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=st.session_state.messages,
                )
                reply = response.choices[0].message.content
                st.markdown(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})
            except Exception as e:
                st.error(f"An error occurred: {e}")
