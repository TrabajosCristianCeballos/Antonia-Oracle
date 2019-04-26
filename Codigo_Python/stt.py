import speech_recognition as sr
from gtts import gTTS
import os
import json

languaje = 'en'
r=sr.Recognizer()
x = int(input("1=normal \n 2=diga antonia \n 3=crearjson \n"))


if x==1:
    while True:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            print("digalo: ")
            audio = r.listen(source,phrase_time_limit=5)
            #audio = r.record(source)

            #audio = r.listen(source)

            try:
                textt = r.recognize_google(audio,show_all=True)
                text1 = r.recognize_google(audio)
                myobj=gTTS(text=str(text1),lang=languaje)

                myobj.save("hola.mp3")
                os.system("ffplay hola.mp3")
                print("3")
                print("posibilidades : {0}".format(textt))
            except:
                print("no entendi...")


elif x==2:
    while True:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source,phrase_time_limit=3)
            try:
                text = r.recognize_google(audio)
                if text == str("Antonia"):
                    print("Hola, que necesitas")
                #print("usted dijo : {0}".format(text))
            except:
                print("no entendi...")

elif x==3:
    while True:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            print("Digalo:")
            audio = r.listen(source,phrase_time_limit=3)

            try:
                text = r.recognize_google(audio)
                jason = {}
                jason['text'] = []
                jason['text'].append({
                    'texto': text
                    })
                with open('data.txt', 'w+') as outfile:
                    json.dump(jason, outfile)

                with open('data.json') as json_file:
                    data = json.load(json_file)
                    for p in data['text']:
                        print('texto: ' + p['texto'])
                        print('')
            except:
                print("no entendi...")






