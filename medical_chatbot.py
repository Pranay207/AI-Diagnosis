import streamlit as st

st.set_page_config(page_title="Simple Medical Bot", page_icon="🩺")
st.title("🩺 Simple Medical Chatbot")
st.markdown("Ask common questions about symptoms or health tips.")

def respond(user_input):
    user_input = user_input.lower()
    if "fever" in user_input:
        return "You may be experiencing an infection. Drink fluids and monitor temperature."
    elif "headache" in user_input:
        return "Try to rest in a dark room. If persistent, consult a doctor."
    elif "cough" in user_input:
        return "A dry cough could be due to cold or allergies. Stay hydrated."
    else:
        return "I'm not sure about that. Please consult a doctor for professional advice."

# Chat UI
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Describe your symptoms...")

if user_input:
    response = respond(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

for speaker, message in st.session_state.chat_history:
    with st.chat_message(speaker.lower()):
        st.markdown(message)
