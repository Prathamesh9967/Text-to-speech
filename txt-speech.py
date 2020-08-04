from gtts import gTTS
import os

f = open('1.txt')
x = f.read().replace("\n"," ")

language = 'en'

audio = gTTS(text=x, lang=language, slow=False)

audio.save('1.mp3')
f.close()
os.system('start 1.mp3')
