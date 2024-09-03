from ast import main
import pyttsx3
import datetime
import speech_recognition as sr
import importlib
module = importlib.import_module('distutils')
import wikipedia
import webbrowser
import os
import  smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    
    speak("I am Jojo Sir. Please tell me how may I help you")

def takeCommand():
    #it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with  sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold= 500
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('heyjayasoni@gmail.com','jojo@789')
    server.sendmail('heyjayasoni@gmail.com', to , content)
    server.close()

if __name__ == "__main__":
   # speak("jaya is a good girl")
   wishMe()
   query = takeCommand().lower()
   #while True:
   if  2:
        
        #logic for executing task based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=10)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stackover" in query:
            webbrowser.open("stackover.com")

        elif "open instagram" in query:
            webbrowser.open("instagram.com")
        
        elif "open geeksforgeeks" in query:
            webbrowser.open("geeksforgeeks.com")

        elif "open w3schools" in query:
            webbrowser.open("w3schools.com")

        elif "open whatsapp" in query:
            webbrowser.open("whatsapp.com")

        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is{strTime} ")

        elif 'open code' in query:
            codePath = "C:\\Users\\Tech\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'email to jaya' in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to = "heyjayasoni@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry my friend Jaya bro. I am not able to send this mail ")