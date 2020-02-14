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
engine.setProperty('voice', voices[1].id)

window = Tk()
window.iconbitmap(r'C:\Users\Nkb\Documents\icon.ico')


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





        elif 'open course era' in query:
            var.set('opening course era')
            window.update()
            speak('opening course era')
            webbrowser.open("coursera.com")

        elif 'open google' in query:
            var.set('opening google')
            window.update()
            speak('opening google')
            webbrowser.open("google.com")

        elif 'open weather' in query:
            var.set('opening weather')
            window.update()
            speak('opening weather')
            webbrowser.open("http://newsrss.bbc.co.uk/weather/forecast/351/Next3DaysRSS.xml")    






        elif 'hello jarvis' in query:
            var.set('Hello Sir')
            window.update()
            speak("Hello Sir")
			
        elif 'open stackoverflow' in query:
            var.set('opening stackoverflow')
            window.update()
            speak('opening stackoverflow')
            webbrowser.open('stackoverflow.com')

        elif 'open instagram' in query:
            var.set('opening instagram')
            window.update()
            speak('opening instagram')
            webbrowser.open('https://www.instagram.com/')    







        elif ('play music' in query) or ('change music' in query):
            var.set('Here are your favorites')
            window.update()
            speak('Here are your favorites')
            music_dir = 'C:\\Users\\Nkb\Desktop\\New folder'  
            songs = os.listdir(music_dir)
            n = random.randint(0,5)
            os.startfile(os.path.join(music_dir, songs[n]))



        elif 'shutdown' in query:  
            shutdown() 

        elif 'restart' in query:
            restart()      

        

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            var.set("Sir the time is %s" % strtime)
            window.update()
            speak("Sir the time is %s" %strtime)

        elif 'the date' in query:
            strdate = datetime.datetime.today().strftime("%d %m %y")
            var.set("Sir today's date is %s" %strdate)
            window.update()
            speak("Sir today's date is %s" %strdate) 

        elif 'thank you jarvis' in query:
            var.set("Welcome Sir")
            window.update()
            speak("Welcome Sir")

        elif 'can you do for me' in query:
            var.set('I can do multiple tasks for you sir. tell me whatever you want to perform sir')
            window.update()
            speak('I can do multiple tasks for you sir. tell me whatever you want to perform sir')

        elif 'old are you' in query:
            var.set("I am a little baby sir")
            window.update()
            speak("I am a little baby sir")

        

        elif 'your name' in query:
            var.set("Myself jarvis Sir")
            window.update()
            speak('myself jarvis sir')

        elif 'who creates you' in query:
            var.set('My Creator is NKB')
            window.update()
            speak('My Creator is NKB')

        elif ' hello' in query:
            var.set('Hello Everyone! My self jarvis')
            window.update()
            speak('Hello Everyone! My self jarvis')

       

        elif 'open chrome' in query:
            var.set("Opening Google Chrome")
            window.update()
            speak("Opening Google Chrome")
            path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" 
            os.startfile(path)



        

        elif 'send email ' in query:
            try:
                var.set("What should I say")
                window.update()
                speak('what should I say')
                content = takeCommand()
                to = 'nboadh0@gmail.com'
                sendemail(to, content)
                var.set('Email has been sent!')
                window.update()
                speak('Email has been sent!')

            except Exception as e:
                print(e)
                var.set("Sorry Sir! I was not able to send this email")
                window.update()
                speak('Sorry Sir! I was not able to send this email')
		

        elif 'open code blocks' in query:
            var.set('Opening Codeblocks')
            window.update()
            speak('opening Codeblocks')
            os.startfile("C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe") 

        elif 'stop' in query:
            speak('by sir')
            speak('have a good day')
            speak('thankyou')
            exit()    




        

        
        elif 'joke' in query:
            var.set('jokes for you sir!')
            
            window.update()
            res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
            if res.status_code == requests.codes.ok:
                var.set(str(res.json()['joke']))
                print(str(res.json()['joke']))
                speak(str(res.json()['joke']))
                
            else:
                speak('oops!I ran out of jokes')    







 

      
   

        

       
        
       
                

def update(ind):
    frame = frames[(ind)%100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)
    window.title('Jarvis')
    
   
    

label2 = Label(window, textvariable = var1, fg = 'purple')
label2.config(font=("Helvetica", 40,'bold'))
var1.set('Jarvis')
label2.pack()

label1 = Label(window, textvariable = var,fg='grey')
label1.config(font=("Helvetica", 30))
var.set('Welcome')
label1.pack()

frames = [PhotoImage(file='C:\\Users\\Nkb\\Downloads\\Assistant.gif',format = 'gif -index %i' %(i)) for i in range(100)]
window.title('Jarvis')

label = Label(window, width = 700, height = 500)
label.pack()
window.after(0, update, 0)

btn0 = Button(text = 'Wish Me',width = 20, command = wishme, bg = 'pink',fg='brown')
btn0.config(font=("Sansserif 11", 15,'bold'))
btn0.pack()
btn1 = Button(text = 'Use Mic',width = 20,command = Ask, bg = 'pink',fg='brown')
btn1.config(font=("Sansserif 11", 15,'bold'))
btn1.pack()
btn2 = Button(text = 'EXIT',width = 20, command = window.destroy, bg = 'pink',fg='brown')
btn2.config(font=("Sansserif 11", 15,'bold'))
btn2.pack()


window.mainloop()