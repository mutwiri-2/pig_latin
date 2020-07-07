import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Enter English text to translate")
    audio = recognizer.listen(source)
    try:
        voice_data = recognizer.recognize_google(audio)
        print(voice_data)
    except sr.UnknownValueError:
        print("Sorry, I did not get that")
    except sr.RequestError:
        print("Sorry, my services are currently down")