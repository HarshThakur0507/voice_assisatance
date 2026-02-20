import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import pyjokes

# Initialize engine once (important)
engine = pyttsx3.init()

def speak(text):
    print(f"Assistant: {text}")
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("Speech output error:", e)

def wish_user():
    hour = datetime.datetime.now().hour
    
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
        
    speak("I am your voice assistant. How can I help you today?")

def take_command():
    try:
        return input("You (type your command): ").lower().strip()
    except:
        return ""

def run_assistant():
    wish_user()
    
    while True:
        query = take_command()

        if not query:
            speak("Please type something.")
            continue

        # Wikipedia Search
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            search_query = query.replace("wikipedia", "").strip()
            
            if search_query == "":
                speak("Please tell me what to search on Wikipedia.")
                continue
            
            try:
                result = wikipedia.summary(search_query, sentences=2)
                speak("According to Wikipedia:")
                speak(result)
            except wikipedia.exceptions.DisambiguationError:
                speak("There are multiple results. Please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find anything on that topic.")
            except Exception as e:
                speak("An error occurred while searching Wikipedia.")

        # Open YouTube
        elif "open youtube" in query:
            speak("Opening YouTube...")
            webbrowser.open("https://www.youtube.com")

        # Open Google
        elif "open google" in query:
            speak("Opening Google...")
            webbrowser.open("https://www.google.com")

        # Tell Time
        elif "time" in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {str_time}")

        # Tell Joke
        elif "joke" in query:
            try:
                joke = pyjokes.get_joke()
                speak(joke)
            except:
                speak("Sorry, I couldn't fetch a joke.")

        # Exit
        elif "exit" in query or "bye" in query:
            speak("Goodbye! Have a nice day!")
            break

        # Unknown command
        else:
            speak("Sorry, I didn't understand that. Try again.")

if __name__ == "__main__":
    run_assistant()
