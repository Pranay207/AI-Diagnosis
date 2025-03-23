import streamlit as st
import openai


# ⛑ Paste your API Key here
openai.api_key = "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"

# Page setup
st.set_page_config(page_title="Medical Chatbot", page_icon="💊")
st.title("💊 Medical Chatbot")
st.markdown("Ask anything about your health symptoms or medical concerns. 🩺\n\n> ⚠️ This is for informational purposes only and not a substitute for professional medical advice.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Type your medical question here...")

if user_input:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # Get assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking... 🤔"):
           client = openai.OpenAI(api_key="sk-...your-api-key-here...")
            response = client.chat.completions.create(
                  model="gpt-3.5-turbo",
                  messages=st.session_state.messages
            )
            reply = response.choices[0].message.content

            st.markdown(reply)

    # Add assistant reply to history
    st.session_state.messages.append({"role": "assistant", "content": reply})
