import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pyjokes
import time

engine = pyttsx3.init()
listening = True   # Control variable

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        return query.lower()
    except:
        return ""

def run_assistant():
    global listening
    speak("Voice assistant activated.")

    while True:

        if listening:
            query = take_command()
        else:
            query = input("Assistant paused. Type 'resume' to continue: ").lower()

            if query == "resume":
                listening = True
                speak("Resuming listening.")
                continue
            else:
                continue

        if "stop listening" in query:
            speak("Okay, I will stop listening. Type resume to continue.")
            listening = False

        elif "open youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif "time" in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {str_time}")

        elif "exit" in query or "bye" in query:
            speak("Goodbye!")
            break

        else:
            speak("I did not understand that command.")

if __name__ == "__main__":
    run_assistant()
