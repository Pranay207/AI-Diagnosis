import streamlit as st

# Page setup
st.set_page_config(page_title="AI  Medical Chatbot", page_icon="💊")
st.title("💊 AI Medical Chatbot")
st.markdown("Ask common health questions. This chatbot works without the internet or APIs!")

# Sample logic-based response system
def get_medical_response(user_input):
    user_input = user_input.lower()
    
    # Common symptom checks
    if "fever" in user_input:
        return "You might have an infection or flu. Stay hydrated and rest. If fever persists for more than 3 days, consult a doctor."
    elif "headache" in user_input:
        return "It could be due to stress, dehydration, or screen time. Drink water and rest. If it continues, please seek medical advice."
    elif "cold" in user_input or "cough" in user_input:
        return "Sounds like a cold or mild flu. Drink warm fluids, rest, and avoid cold environments."
    elif "stomach" in user_input or "pain" in user_input:
        return "Stomach pain can have many causes like gas, infection, or food poisoning. Monitor symptoms and stay hydrated."
    elif "covid" in user_input:
        return "If you suspect COVID-19, isolate yourself and get tested. Look out for symptoms like fever, cough, and breathing difficulty."
    elif "tired" in user_input or "fatigue" in user_input:
        return "Fatigue may be due to lack of sleep, nutrition, or stress. Consider your lifestyle and rest well."
    elif "hello" in user_input or "hi" in user_input:
        return "Hello! I'm your health assistant. How can I help you today?"
    else:
        return "Sorry, I don't have enough information on that. Please consult a medical professional for a better diagnosis."

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input from user
user_input = st.chat_input("Type your medical question here...")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get bot response
    response = get_medical_response(user_input)
    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
