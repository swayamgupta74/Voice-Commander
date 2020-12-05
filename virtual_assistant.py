import pyttsx3
import os
import webbrowser
import speech_recognition as sr
import wikipedia
import time

def media():
	pyttsx3.speak("opening media player")
	os.system("start wmplayer")
def paint():
	pyttsx3.speak("opening paint")
	os.system("start mspaint")
def python():
	pyttsx3.speak("opening python shell")
	os.system("start python")
def excel():
	pyttsx3.speak("opening excel")
	os.system("start excel")
def cmd():
        pyttsx3.speak("opening command prompt")
        os.system("start cmd")
def camera():
	pyttsx3.speak("opening camera")
	os.system("start microsoft.windows.camera:")
def chrome():
	pyttsx3.speak("opening chrome")
	os.system("start chrome")
def notepad():
	pyttsx3.speak("opening notepad")
	os.system("start notepad")
def photoviewer():
	pyttsx3.speak("opening photo viewer")
	os.system("start WindowsPhotoViewer")
def appstore():
	pyttsx3.speak("opening app store")
	os.system("start pcappstore")
def microsoftedge():
	pyttsx3.speak("opening microsoft edge")
	os.system("start msedge")
def facebook():
	pyttsx3.speak("opening facebook")
	os.system("start chrome www.facebook.com")
def youtube():
	pyttsx3.speak("opening youtube")
	os.system("start chrome www.youtube.com")
def instagram():
	pyttsx3.speak("opening instagram")
	os.system("start chrome www.instagram.com")
def linkedin():
	pyttsx3.speak("opening linkedin")
	os.system("start chrome www.linkedin.com")
def twitter():
	pyttsx3.speak("opening twitter")
	os.system("start chrome www.twitter.com")
def gmail():
	pyttsx3.speak("opening gmail")
	os.system("start chrome www.gmail.com")
def github():
	pyttsx3.speak("opening github")
	os.system("start chrome https://github.com/login")
def shutdown():
	pyttsx3.speak("powering off")
	os.system("shutdown /s /t 1")

pyttsx3.speak("Hello  ")
pyttsx3.speak("what is your name")
r = sr.Recognizer()
with sr.Microphone() as source:
    print("listening")
    pyttsx3.speak("listening ")
    audio=r.listen(source)
    print("stop listening")
    pyttsx3.speak("done")
name =r.recognize_google(audio)
pyttsx3.speak("Hi "+name)
print("Hi "+name)


while True:   
    r1 = sr.Recognizer()
    r2 = sr.Recognizer()
    with sr.Microphone() as source:
        pyttsx3.speak("what can i do for you")
        print("listening")
        pyttsx3.speak("listening")
        audio=r1.listen(source)
        print("stop listening")
        pyttsx3.speak("done")
    command =r1.recognize_google(audio)
    command=command.lower()
    print(command)
    
    if ("wikipedia" in command):
        while True:
       
            pyttsx3.speak("what you want to search")
	    
            with sr.Microphone() as source:
                print("listening")
                pyttsx3.speak("listening ")
                audio=r2.listen(source)
                print("stop listening")
                pyttsx3.speak("done")
            search=r2.recognize_google(audio)
            pyttsx3.speak("searching "+search) 
            result=wikipedia.summary(search,sentences=2)
            print()
            print(result)
            pyttsx3.speak(result)
            break
       
    elif (("run" in command) or ("open" in command)) and ("media" in command) and ("player" in command):
        media()
    elif (("run" in command) or ("open" in command)) and ("paint" in command):
        paint()
    elif ("open" in command) and ("python" in command):
        python()
    elif (("run" in command) or ("open" in command)) and ("excel" in command):
        excel()
    elif (("run" in command) or ("open" in command)) and ("cmd" in command):
        cmd()
    elif (("run" in command) or ("open" in command)) and ("camera" in command):
        camera()
    elif (("run" in command) or ("open" in command)) and ("chrome" in command):
            chrome()
    elif (("run" in command) or ("open" in command)) and ("notepad" in command):
        notepad()
    elif (("run" in command) or ("open" in command)) and (("photo" in command) and ("viewer" in command)):
        photoviewer()
    elif (("run" in command) or ("open" in command)) and (("app" in command) and ("store" in command)) :
        appstore()
    elif (("run" in command) or ("open" in command)) and (("microsoft edge" in command) or ("edge" in command)):
            microsoftedge()
    elif (("run" in command) or ("open" in command)) and ("facebook" in command):
            facebook()
    elif (("run" in command) or ("open" in command)) and ("youtube" in command):
            youtube()
    elif (("run" in command) or ("open" in command)) and ("instagram" in command):
            instagram()	   
    elif (("run" in command) or ("open" in command)) and ("linkedin" in command):
            linkedin()
    elif (("run" in command) or ("open" in command)) and ("twitter" in command):
            twitter() 	
    elif (("run" in command) or ("open" in command)) and ("gmail" in command):
            gmail() 
    elif (("run" in command) or ("open" in command)) and ("github" in command):
            github() 	
    elif ("shutdown" in command) and ("pc" in command):
            shutdown() 	
    elif (("run" in command) or ("open" in command)) and ("whatsapp" in command):
            os.system("start chrome https://web.whatsapp.com/") 
    elif ("close" in command) or ("exit" in command) or ("nothing" in command) or("quit" in command):
        break 
    else:
        pyttsx3.speak("Sorry I cant do "+command+"for you")
        print("Sorry I cant do this for you.")
 
