import speech_recognition as sr
import pyttsx3
# needs pyaudio
engine = pyttsx3.init()

def say(str):
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(str)
    engine.runAndWait()
    engine.stop()


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        say("I am Listening")
        recognizer.adjust_for_ambient_noise(source)
        try:
            # , timeout=20, phrase_time_limit=10
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            say("You said: " + text)
            return text
        except sr.UnknownValueError:
            say("Please try again")
            listen()
        except sr.WaitTimeoutError:
            say("Please say something")
            listen()
        except sr.RequestError as e:
            say("Could not request results from Google Speech Recognition service. Try later")
            return ''

