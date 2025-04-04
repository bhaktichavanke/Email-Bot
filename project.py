import smtplib
import speech_recognition as sr
import pyaudio
import pyttsx3
from email.message import EmailMessage


listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info  # or u can use info.lower()
    except:
        pass

def sendmail(name, subject, text):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('chavankebhakti22@gmail.com', 'ouhs qgzj lrup ckzg')
    email = EmailMessage()
    email['From'] = 'chavankebhakti22@gmail.com'
    email['To'] = name
    email['Subject'] = subject
    email.set_content(text)
    server.send_message(email)
    # server.sendmail('chavankebhakti22@gmail.com',
    #                 name,
    #                 'hi dude how are you i was waiting ')

email_list = {
    'bhakti' : 'chavankebhakti2003@gmail.com',
    'anjali' : 'anjalisiya2003@gmail.com'
}

def get_email_info():
    print('To whome you want to send an email?')
    talk('to whom you want to send an email ')
    name = get_info()
    receiver = email_list[name]
    print('what is the subject of your email?')
    talk('what is the subject of your email?')
    subject = get_info()
    print('Tell me the body of the email')
    talk('Tell me the body of the email')
    message = get_info()
    sendmail(receiver, subject, message)
    print('do you want to send more emails?')
    talk('do you want to send more emails?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()