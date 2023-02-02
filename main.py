from time import sleep
import speech_recognition as sr
from pynput.keyboard import Key, Controller
r = sr.Recognizer()
r1 = sr.Recognizer()
mic = sr.Microphone()
 
keyboard = Controller()

#if you want more things to react with it, you can add anything with; 'TEXT', so for example,  ",'surrender'" (remember, has to be lowercase)
key_words = ['down', 'get down', 'ground', "hands up"]

while True:
    with sr.Microphone() as source: #select main mic
        r.adjust_for_ambient_noise(source) #adjust
        try:
            aud = r.listen(source,timeout=3) #listen for 3 seconds
            try: 
               if r.recognize_google(aud, language='en-US') in key_words:
                   keyboard.press('f')
                   sleep(0.2)
                   keyboard.release('f')
                   print('get down found')
               else:
                   print('not detected')
            except sr.UnknownValueError: #I do not know what this exception was, but it has to be here
                print('error 1')
            except sr.RequestError: #If it fails to get the request
                print('error 2')
        except sr.WaitTimeoutError: #Time out from google
            print('Timed out')
