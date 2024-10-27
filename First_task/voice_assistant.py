import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import random

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to user input via microphone."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            return None
        except sr.RequestError:
            print("Sorry, the service is down.")
            return None
        return query.lower()

def respond_to_command(query):
    """Respond to user queries."""
    if query is None:
        speak("Sorry, I didn't understand. Could you please repeat?")
        return True

    if "time" in query:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {current_time}")
    
    elif "wikipedia" in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        try:
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(result)
        except wikipedia.exceptions.DisambiguationError:
            speak("There are multiple results, please be more specific.")
        except wikipedia.exceptions.PageError:
            speak("I couldn't find anything on that topic.")
    
    elif "your name" in query:
        speak("My name is Python Voice Assistant.")
    
    elif "hi" in query or "hello" in query:
        responses = ["Hello! How can I assist you today?", "Hi there! What can I do for you?"]
        speak(random.choice(responses))

    elif "exit" in query or "bye" in query:
        speak("Goodbye! Have a nice day.")
        return False

    else:
        # Fallback response for unrecognized commands
        responses = [
            "I'm sorry, I don't know the answer to that.",
            "Can you please rephrase your question?",
            "Hmm, I'm not sure how to respond to that."
        ]
        speak(random.choice(responses))
    
    return True

# Main loop
if __name__ == "__main__":
    while True:
        command = listen()
        if not respond_to_command(command):
            break
