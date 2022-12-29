import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import speech_recognition as sr
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am marco....please tell How may I help you?")

def takeCommand():
    # it take command using microphone and return string
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        r.energy_threshold=1000
        r.adjust_for_ambient_noise(source,1.2)
        print("Listening...")
        audio=r.listen(source)

    try:
        print("recognizing..")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        speak("Please! Say it again..")
        return "None"
    return query.lower()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('amanshrivastav0303200@gmail.com', 'Aman@#%9457')
    server.sendmail('amanshrivastav0303200@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
    
        query=takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  


        #elif 'play music' in query:
          #  music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
          #  songs = os.listdir(music_dir)
           # print(songs)    
           # os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Aman\\AppData\\Lenavo\\Programs\\VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "singhabhishek070801@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")    

    
