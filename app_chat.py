import pyttsx3
import time
import sys

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 170)  # Speech speed

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def type_text(text):
    """Simulate typing effect for bot output."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)  # Delay between characters
    print()  # New line after text

def chatbot_response(user_input):
    """Rule-based chatbot logic."""
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm doing great, thanks for asking!"
    elif "your name" in user_input:
        return "I am your Broskieshub chatbot assistant."
    elif "who created you?" in user_input:
        return "Basheer created me."
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I don't understand that."

def main():
    print("💬 Chatbot is ready! Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower().strip()

        if not user_input:
            continue

        response = chatbot_response(user_input)
        type_text(f"Bot: {response}")  # Typing effect
        speak(response)  # Speak the response

        if "bye" in user_input:
            break

if __name__ == "__main__":
    main()
