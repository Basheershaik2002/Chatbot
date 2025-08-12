import time
import streamlit as st
from datetime import datetime
import random
import webbrowser

def chatbot_response(user_input):
    """Rule-based chatbot logic."""
    # Greetings
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm doing great, thanks for asking!"
    
    # About chatbot
    elif "your name" in user_input:
        return "I am your Broskieshub chatbot assistant."
    elif "who created you" in user_input:
        return "Basheer created me."
    elif "broskieshub" in user_input:
        return "Broskieshub is a platform created by Basheer for sharing knowledge, learning new skills, and building a tech community."
    
    # Time & Date
    elif "time" in user_input:
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}."
    elif "date" in user_input:
        current_date = datetime.now().strftime("%A, %B %d, %Y")
        return f"Today's date is {current_date}."
    
    # Joke
    elif "joke" in user_input:
        jokes = [
            "Why don’t skeletons fight each other? They don’t have the guts.",
            "I told my computer I needed a break, and it froze.",
            "Why did the math book look sad? Because it had too many problems.",
            "Why do programmers prefer dark mode? Because light attracts bugs!"
        ]
        return random.choice(jokes)
    
    # Open browser
    elif "open browser" in user_input:
        webbrowser.open("https://www.google.com")
        return "Opening your browser..."
    
    # Goodbye
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    
    else:
        return "Sorry, I don't understand that."

# Streamlit app UI
st.set_page_config(page_title="Broskieshub Chatbot", page_icon="💬", layout="centered")
st.title("💬 Broskieshub Chatbot")
st.markdown("Type your message below and get a reply!")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.text_input("You:", key="input")

if st.button("Send") and user_input.strip() != "":
    # Add user message
    st.session_state.messages.append(("You", user_input))
    
    # Bot reply
    bot_reply = chatbot_response(user_input.lower())
    st.session_state.messages.append(("Bot", bot_reply))

# Display chat history
for sender, msg in st.session_state.messages:
    if sender == "You":
        st.markdown(f"**You:** {msg}")
    else:
        with st.spinner("Bot is typing..."):
            time.sleep(1)
        st.markdown(f"**🤖 Bot:** {msg}")
