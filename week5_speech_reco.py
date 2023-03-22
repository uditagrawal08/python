import speech_recognition as sr
AUDIO_FILE=("udit.wav")
r=sr.Recognizer()
#initialize the recognizer
with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source)
    #reads the audio file
try :
    print("audio file cotains"+r.recognize_google(audio))
except sr.UnknownValueError:
    print("google speech recogintion is not understand")
except sr.RequestError:
    print("could not get value from google")
        
