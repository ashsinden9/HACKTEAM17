from tkinter import *
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import roman
import sys
import requests
import re
import threading



numbers = {'hundred':100, 'thousand':1000, 'lakh':100000}
a = {'Sam':'nboadh0@gmail.com'}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

window = Tk()

global var
global var1

var = StringVar()
var1 = StringVar()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('vishalhanda005@gmail.com', 'lucifer511') 
    server.sendmail('nboadh0@gmail.com', to, content)
    server.close()

def shutdown():
    speak('understood sir')
    speak('connecting to command prompt')
    speak('shutting down your computer')
    os.system('shutdown -s') 

def restart():
    speak('understood sir')
    speak('connecting to command prompt')
    speak('shutting down your computer')
    os.system('shutdown -r')     

    


def goofline():
    speak('okey sir')
    speak('closing all systems')
    speak('disconnecting to servers')
    speak('going offline')
    quit()  

def online():
    speak('okey sir')
    speak('starting all system applications')
    speak('installing all drivers')
    speak('every drivers is intalled')
    speak('all system have been started')
    speak('now i am online sir')    









def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        var.set("Good Morning Sir")
        window.update()
        speak("Good Morning Sir!")

        



    elif hour >= 12 and hour <= 18:
        var.set("Good Afternoon Sir!")
        window.update()
        speak("Good Afternoon Sir!")
              


    else:
        var.set("Good Evening Sir")
        window.update()
        speak("Good Evening Sir!")
        



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        return "None"
    var1.set(query)
    window.update()
    return query

def Ask():
    btn2['state'] = 'disabled'
    btn0['state'] = 'disabled'
    btn1.configure(bg = 'yellow')
    wishme()
    while True:
        btn1.configure(bg = 'yellow')
        query = takeCommand().lower()
        if 'exit' in query:
            var.set("Bye sir")
            btn1.configure(bg = 'yellow')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            window.update()
            speak("Bye sir")
            break

        elif 'wikipedia' in query:
            if 'open wikipedia' in query:
                webbrowser.open('wikipedia.com')
            else:
                try:
                    speak("searching wikipedia")
                    query = query.replace("according to wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to wikipedia")
                    var.set(results)
                    window.update()
                    speak(results)
                except Exception as e:
                    var.set('sorry sir could not find any results')
                    window.update()
                    speak('sorry sir could not find any results')

        elif 'open youtube' in query:
            var.set('opening Youtube')
            window.update()
            speak('opening Youtube')
            webbrowser.open("youtube.com")

        elif 'close youtube' in query:
            os.system("taskill /im youtube.com /f")    





        elif 'google search' in query:
            var.set('opening Google')
            window.update()
            speak('opening Google')
            webbrowser.open("http://www.google.co.in/search?q=")   

        elif 'sing a song' in query:
            var.set('Twinkle, twinkle, little star How I wonder what you are Up above the world so high Like a diamond in the sky Twinkle')
            window.update()
            speak('Twinkle, twinkle, little star How I wonder what you are Up above the world so high Like a diamond in the sky Twinkle, twinkle little star How I wonder what you are')     

