import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
import subprocess
import wikipedia
import smtplib

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Recognizing...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        print("Could not understand audio, Try again!!")
        speak("Could not understand audio, Try again!!")
        return listen()
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

if __name__ == '__main__':
    print("Welcome to Bosom A.I.")
    speak("Welcome to Bosom A.I. How may I help You sir??")
    while True:
        print("Listening...")
        query = listen()
        print(f"User said: {query}\n")
        #if f"Open {site[0]}".lower() in query.lower():
        # todo: Add more sites
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speak(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        if 'play music' in query:
            speak("Playing music Sir")
            print("Playing music Sir")
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join( music_dir, songs[0]))

        elif "send email".lower() in query.lower():
            from email.mime.text import MIMEText
            from email.mime.multipart import MIMEMultipart
            from confidential import password


             # Email configuration
            sender_email = 'mridulnavgotri2508@gmail.com'
            receiver_email = 'mridulnavgotri2508@gmail.com'

            # Create message
            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = receiver_email
            speak("What is the subject")
            print("What is the subject")
            message['Subject'] = listen()
            print(message)

            # Add body to email
            speak("What is the body for your mail?")
            print("What is the body for your mail?")
            body = listen()
            print(body)
            message.attach(MIMEText(body, 'plain'))

            # Connect to SMTP server
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()  # Start TLS encryption
                server.login(sender_email, password)
                text = message.as_string()
                server.sendmail(sender_email, receiver_email, text)

            print("Email sent successfully!")
            speak("Email sent successfully!")

        elif "question".lower() in query.lower():  #if wikipedia found in the query then this block will be executed

            speak("What is ur question ")
            query = listen()
            print(query)

            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open camera".lower() in query.lower():
            speak("Opening camera")
            subprocess.run('start microsoft.windows.camera:', shell=True)
            speak("Opened the camera")

        elif "time".lower() in query.lower():
            hour = int(datetime.datetime.now().strftime("%H"))
            min = int(datetime.datetime.now().strftime("%M"))
            if hour>=0 and hour<12:
                speak(f"Good morning, the time is {hour} hours and {min} minutes ")
            elif hour>=12 and hour<18:
                speak(f"Good afternoon, the time is {hour} hours and {min} minutes ")
            else:
                speak(f"Good evening, the times is {hour} hours and {min} minutes ")


        elif "open app".lower() in query.lower():
            os.startfile(os.path.join("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"))
            speak("Opened the app Sir")

        elif "Quit right now".lower() in query.lower():
            speak("Have a great day, Goodbye!!")
            exit()

        else:
            print("Sorry unable to understand, Please try again")
            speak("Sorry unable to understand, Please try again")



