import pyttsx3
import os
pyttsx3.speak("Please enter your name")
name=input(" Please enter your name  :")
pyttsx3.speak("Hi "+name)
print(" Hi"+name)
pyttsx3.speak("Hey This is swayam what can i do for you ")
while True:
	
	command=input("What can i do for you  :  ")

	if (("run" in command) or ("open" in command)) and ("media" in command) and ("player" in command):
	    os.system("start wmplayer")
	elif (("run" in command) or ("open" in command)) and ("chrome" in command):
            os.system("start chrome")
	elif (("run" in command) or ("open" in command)) and ("notepad" in command):
	    os.system("start notepad")
	elif (("run" in command) or ("open" in command)) and (("photo" in command) and ("viewer" in command)):
	    os.system("start WindowsPhotoViewer")
	elif (("run" in command) or ("open" in command)) and (("app" in command) and ("store" in command)) :
	    os.system("start pcappstore")
	elif (("run" in command) or ("open" in command)) and (("microsoft" in command) and ("edge" in command)):
            os.system("start msedge")
	elif (("run" in command) or ("open" in command)) and ("facebook" in command):
            os.system("start chrome www.facebook.com")
	elif (("run" in command) or ("open" in command)) and ("youtube" in command):
            os.system("start chrome www.youtube.com")
	elif (("run" in command) or ("open" in command)) and ("instagram" in command):
            os.system("start chrome www.instagram.com")	   
	elif (("run" in command) or ("open" in command)) and ("linkedin" in command):
            os.system("start chrome www.linkedin.com")
	elif (("run" in command) or ("open" in command)) and ("twitter" in command):
            os.system("start chrome www.twitter.com") 	
	elif (("run" in command) or ("open" in command)) and ("gmail" in command):
            os.system("start chrome www.gmail.com") 
	elif (("run" in command) or ("open" in command)) and ("github" in command):
            os.system("start chrome https://github.com/login") 	
	elif ("shutdown" in command) and ("pc" in command):
            os.system("shutdown /s /t 1") 	
	elif (("run" in command) or ("open" in command)) and ("whatsapp" in command):
            os.system("start chrome https://web.whatsapp.com/") 
  	
	elif ("close" in command) or ("exit" in command):
	    break 
	else:
	    pyttsx3.speak("Sorry I cant do "+command+"for you")
	    print("Sorry I cant do this for you.")
 