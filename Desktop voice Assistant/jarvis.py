import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install speech Recognition 
import wikipedia # pip install wikipedia
import webbrowser #pip install web browser
import random
import os 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Made function that allowed Jarvis voice to say in output. 
def speek(audio):
    engine.say(audio)
    engine.runAndWait()

# " Below function assign to specific tasks with timining and giving output with jarvis voice.    "
def JarvisIntro():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speek("Good Morning")

    elif hour >= 12 and hour < 18:
        speek("Good Afternoon")

    else:
        speek("Good Evening")

    speek("I'm jarvis. How Can I Assist you today?")

    # "This below function recognize microphone Input from the user and return string output. "
def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listeninig................")
        r.pause_threshold = 1
        audio = r.listen(source)
   
    try:
        print("Recognizing.........")
        query = r.recognize_google(audio, language='en-us')
        print(f"User said: {query}\n")
    
    except Exception as e:
        speek ("Say that again please.......")
        print ("Say that again please.......")
        return "none"
    return query
        
if __name__ == "__main__":
    JarvisIntro()   
    while True:
        query = takeCommand().lower()   

        # Logic for executing task based on query
        
        if 'wikipedia' in query:
            speek("searching your results ..............")
            query = query.replace("wikipedia ", " ")
            result = wikipedia.summary(query, sentences=2)
            speek("According to wikipedia")
            print(result)
            speek(result)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'open google' in query:
            webbrowser.open("Google.com")

        elif 'play music' in query:
            speek("for sure!!")
            path = 'E:\\music'
            songs = os.listdir(path)
            d=random.choice(songs)
            os.startfile(os.path.join(path, d))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I: %M: %p")
            print(strTime)
            speek(f"The time is {strTime}")
        
        elif 'open code' in query:
            openpath = "C:\\Users\\WIN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(openpath)
        
        elif 'exit' in query:
            speek('okay!!!')
            exit()