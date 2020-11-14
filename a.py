import smtplib

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

sender_email = 'krisme4545@gmail.com'
password = 'FUCKYOU4545'
receiver = 'krishnakant08hati@gmail.com'

r = sr.Recognizer()
mic = sr.Microphone()


tts = gTTS('What is the subject of the email')
tts.save('subject.mp3')
playsound('subject.mp3')
with mic as source:
    audio = r.listen(source)
subject = r.recognize_google(audio)
print(f'THE subject is : {subject}')

print("THe content")
with mic as source:
    audio = r.listen(source)

body_of_the_email = r.recognize_google(audio)
tts = gTTS(body_of_the_email)
tts.save('body_of_the_email.mp3')
print(f'You said: {body_of_the_email}')
playsound('body_of_the_email.mp3')

content = "Subject: {}\n\n{}".format(subject, body_of_the_email)

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, password)

#Login is authorised

print("Login success")

server.sendmail(sender_email, receiver, content)
print("Email sent to the receiver")
