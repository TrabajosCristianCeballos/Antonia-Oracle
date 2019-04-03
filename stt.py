import speech_recognition as sr
from gtts import gTTS
import os


languaje = 'en'
r=sr.Recognizer()
x = int(input("1 0 2 \n"))


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


else:
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





# import pip
# installed_packages = pip.get_installed_distributions()
# installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
#      for i in installed_packages])
# print(installed_packages_list)
