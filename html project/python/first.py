from gtts import gTTS
import Playsound

#get user input
text=input("enter your text")

#convert text to speech
sound=gTTS(text,lang="en")