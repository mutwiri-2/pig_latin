import time
import os
import random
from pig_latin import pig_latin
import speech_recognition as sr
import playsound
from gtts import gTTS

recognizer = sr.Recognizer()

def record_audio():
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
        voice_data = ''
        try:
            voice_data = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            speak("Sorry, I did not get that")
        except sr.RequestError:
            speak("Sorry, my services are currently down")
        return voice_data

def translate(voice_data):
    translated_text = pig_latin(voice_data)
    speak(translated_text)

def speak(audio_string):
    text_to_speech = gTTS(text=audio_string, lang='en')
    num = random.randint(1,10000000)
    audio_file = 'audio-' + str(num) + '.mp3'
    text_to_speech.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)

time.sleep(1)
speak("Enter English text to translate to pig latin")
while True:
    voice_data = record_audio()
    translate(voice_data)