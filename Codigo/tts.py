from gtts import gTTS #libreria para llevar el texto a un audio
import os #libreria para correr el aduio desde la consola, esta libreria permite correr unos commandos de consola
import json #lireria para cargar json
from translate import Translator # libreria para traducir del español al ingles
from PIL import Image
import random


#if x==1:

class Tts:
    def traducir(self,respuesta):
        translator = Translator(from_lang="english",to_lang="spanish")
        palabra = translator.translate(respuesta)

        return palabra


    def __init__(self):
        #Lista para buscar estas palabras en la respuesta
        #y cargar una imagen relacionada
        lista = [
        "arepa",
        "audio guide",
        "bakery pastery"
        "bandeja paisa",
        "bike tour",
        "brand coffe",
        "chiva tour",
        "coffe crop coffe cultivation",
        "coffe experience",
        "coffe tasting",
        "coffe tour",
        "echange languajes",
        "fruit vegetable",
        "gastronomy comuna 13",
        "handcrafts",
        ]
        #cargamos el archivo de la nube y sacamos la informacionque necesitamos
        #en este caso el query inicial y el texto que se debe hablar
        with open('cloud.json') as json_file:
            data = json.load(json_file)

            #en respuesta se guarda lo que responde el digital assitant
            respuesta = data['text']

            #en texto se saca el query inicial que se hizo en el stt y se guarda para
            #luego mostrar un imagen correspondiente con lo que se quiere
            texto = data['channelExtensions']['debugInfo']['variables']['iResult']['query']



        #aqui se saca el lenguaje inicial del query desde lang.json que es creado con el unico fin
        #de saber en que lenguaje se hizo el query inicial
        with open('lang.json') as json_file:
            data = json.load(json_file)
            languaje = data["lang"][0]

        if languaje == "esp":
            #respuestafinal es la variable en la cual se va a guardar el texto final en el idioma
            #correspondiente y se llevara a audio
            lang = "es"
            respuestafinal = self.traducir(respuesta)
        else:
            lang="en"
            repuestafinal = respuesta

        try:
            myobj=gTTS(text=respuestafinal,lang=lang)
            myobj.save("hola.mp3")
            os.system("ffplay hola.mp3")

            flag = True
            for i in lista:
                if i in respuesta:
                    while flag:
                        try:
                            ruta ='./imagenes/{0}/{1}.jpg'.format(i,random.randint(1,6))
                            image = Image.open(ruta)
                            image.show()
                            flag = False
                        except Exception as e: print(e)
                else:
                    continue

                if not flag:
                    break
                else :
                    continue

        except Exception as e: print(e)



Tts()
