from gtts import gTTS
from playsound import playsound

myText = "Hey I am Generated Text to Speech"
language = "en"
myobj = gTTS(text=myText, lang=language, slow=False)
myobj.save("Output.mp3")
playsound("Output.mp3")
