import smtplib

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

sender_email = 'krisme4545@gmail.com'
password = 'FUCKYOU4545'
receiver = 'krishnakant08hati@gmail.com'

r = sr.Recognizer()
mic = sr.Microphone()


tts = gTTS('What has to be the subject of your Eamil')
tts.save('subject.mp3')
playsound('subject.mp3')
with mic as source:
    audio = r.listen(source)
subject_said = r.recognize_google(audio)
print(f'You said: {subject_said}')
tts = gTTS('You said ' + subject_said)
tts.save('subject_said.mp3')
playsound('subject_said.mp3')

tts = gTTS('What has to be the body of your Eamil')
tts.save('body.mp3')
playsound('body.mp3')
with mic as source:
    audio = r.listen(source)
body_said = r.recognize_google(audio)
tts = gTTS('You said ' + body_said)
tts.save('body_said.mp3')
print(f'You said : {body_said}')
playsound('body_said.mp3')

content = "Subject: {}\n\n{}".format(subject_said, body_said)

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, password)

print("Login success")

server.sendmail(sender_email, receiver, content)
print("Email sent to the receiver")
