import pyttsx3
import webbrowser
import smtplib
import random
import requests
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
from ecapture import ecapture as ec
from twilio.rest import Client
import os
import sys

engine = pyttsx3.init()

client = wolframalpha.Client('whatsapp lo septa')

# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('DUDE: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hello .,DUDE at your service.')
speak('Please tell me how can I help you?')


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry .! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query
        

if __name__ == '__main__':

    while True:
    
        query = myCommand()
        query = query.lower()
        
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what is up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))
        
        elif "camera" in query or "take a photo" in query:
            ec.capture(0, " DUDE Camera ", "img.jpg")
        
        elif "who i am" in query:
            speak("If you talk then definately your human.")
 
        elif "why was you created" in query:
            speak("Thanks to team DUDE. further It's a secret")
        
        elif "who are you" in query:
            speak("I am your virtual assistant created by Team DUDE")
 
        elif 'reason for you' in query:
            speak("I was created as a Minor project by Team DUDE ")
 
        # elif 'change background' in query:
        #     ctypes.windll.user32.SystemParametersInfoW(20, 
        #                                                0, 
        #                                                "Location of wallpaper",
        #                                                0)

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'I am' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry ! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye ., have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello .')

        elif 'bye' in query:
            speak('Bye ., have a good day.')
            sys.exit()
                                    
        elif 'play music' in query:
            speak('Sorry!Oonly from local disc i can play music! Say okay! if I should play the music I have!')
            local = myCommand()

            if 'ok' in local:
                try:
                    speak('playing')
                    n = random.randint(0,2)
                    print(n)

                    music_dir = r'C:\Users\home\Music'
                    song = os.listdir(music_dir)
                    print(song)

                    os.startfile(os.path.join(music_dir,song[n]))

                except:
                    speak('sorry creater was dumb, cant play music, enjoy asking something else.')
        
        elif 'send message' in query:
            speak('i can only send your message to team DUDE contacts. if okay say yes to proceed.')
            local = myCommand()
            if 'yes' in local:
                try:

                    speak(' tell me your message please.')
                    m = myCommand()

                    def send_sms(number, myCommand):
                        url = 'https://www.fast2sms.com/dev/bulk'
                        params = {
                            'authorization': 'paste auth key of msgng api',
                            'sender_id': 'FastWP',
                            'message': myCommand,
                            'language': 'english',
                            'route': 'p',
                            'numbers': number
                        }
                        response = requests.get(url, params=params)
                        dic = response.json()
                        print(dic)
                    
                    send_sms("7032972977,8501024681,8074308757,7207775759", myCommand= m)

                except:
                    speak('creator was dumb. failed to send your mesaage sorry. enjoy asking anything else to your DUDE.')               

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Next Command! Please!')
