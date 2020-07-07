import speech_recognition as sr

recognizer = sr.Recognizer()

def record_audio():
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
        voice_data = ''
        try:
            voice_data = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            print("Sorry, I did not get that")
        except sr.RequestError:
            print("Sorry, my services are currently down")
        return voice_data

print("Enter English text to translate to pig latin")
voice_data = record_audio()
print(voice_data)