import speech_recognition as s
sr=s.Recognizer()
print("try to say something....")
with s.Microphone() as m:
    audio=sr.listen(m)
    query=sr.recognize_google(audio,language='eng-in')
    print(query)
  