#!/usr/bin/env python3
import speech_recognition as sr  #libreria para reconocimiento de voz
import json #libreria para manejo de json
from langdetect import detect_langs #libreria para detectar que idioma se reconocio
from translate import Translator # libreria para traducir del español al ingles
español = 'es-CO'
ingles = ' en-US'
r=sr.Recognizer()

#    print("metodo traducir   "+str(español[x][str(x)]))

class Tts:
    #metodo para traducir las lista de palabras en español a ingles
    def traducir(self,español):
        nueva=[]
        for x in range(0,4):
            try:
                translator = Translator(from_lang="spanish",to_lang="english")
                palabra = translator.translate(español[x][str(x)])
                nueva.append({
                        str(x):palabra
                    })
            except Exception as e: print(e)
        return nueva

    #metodo recibe 2 variables, una lista de maximo 4 de cada una de las posibilidades de cada lenguaje
    def DeterminarLenguaje(self,esp,ing):
        idioma=[]
        # español
        # para saber que idioma es, es usa detect_lang, el problema
        # es que dice un % pero no asegura que sea el lenguaje correcto, por ahora se hacen pruebas
        # con contadores, cada vez que una oracion

        #esta 4 variables son el % de acierto con el idioma, entre mas cercano quude max de 1 y entre mas cerca del 0
        #quede min, mas probables es que sea ese lenguaje
        maxingles=0
        maxespañol=0
        miningles=1
        minespañol=1
        #los contadores son cuantas veces cambia el mejor max de cada uno de los lenguajes
        #hasta ahora parecen ser la mejor forma de saber que leguaje es
        conte=0
        conti=0
        #se agrega a idioma los resultados de detect_langs de las palabras en español
        #ej [[es:098989898],[pt:0.90009]]
        for x in range(0,4):
            try:
                idioma.append(detect_langs(esp[x][str(x)]))
            except Exception as e: print(e)
        #se agrega a idioma los resultados de detect_langs de las palabras en ingles
        for x in range(0,4):
            try:
                idioma.append(detect_langs(ing[x][str(x)]))
            except Exception as e: print(e)
        #aqui se determina los valores de las variables max, min y cont
        #se toma del ejemplo de arriba y si la oracion fue detectada en español o ingles entra
        #en caso de que no sea ninguno de estos no se hace nada
        for x in idioma:
            p=str(x)
            if p[1:3] == 'es':
                if float(p[4:18]) > maxespañol:
                    conte+=1
                    maxespañol = float(p[4:18])

                if float(p[4:18]) < minespañol:
                    minespañol = float(p[4:18])

            elif p[1:3] =='en':
                if float(p[4:18]) > maxingles:
                    conti+=1
                    maxingles = float(p[4:18])

                if float(p[4:18]) < miningles:
                    miningles = float(p[4:18])

        print("maxespañol "+str(maxespañol))
        print("minespañol "+str(minespañol))
        print("maxingles "+str(maxingles))
        print("maxingles "+str(miningles))
        print("contador español "+str(conte))
        print("contador ingles "+str(conti))

        #aqui se determina  que lenguaje es, todavia esta en fase de pruebas
        if maxingles == 0 and miningles == 1:
            return "esp"
        elif maxespañol == 0 and miningles == 1:
            return "ing"
        elif conte > conti:
            return "esp"
        else: return "ing"



    def __init__(self):
        while True:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1) #nivela el microfono segun el ruido del ambiente
                print("Digalo:")
                audio = r.listen(source,phrase_time_limit=3) #el microfono recibe audio durante 3 segundos
                #definicion de variables
                idioma= []  #lista donde se agregan los % de idioma que reconoce el langdetect
                jason = {} #variable donde se vana  guardar los valores del json
                ingles = {}#aqui se guardan los resultados en ingles del reconocimiento de voz
                español = {}#aqui se guardan los resultados en español del reconocimiento de voz
                español['text'] = []
                try:
                    #reconocer voz español
                    text = r.recognize_google(audio,language = "es-CO");
                    posibilidades = r.recognize_google(audio,language = "es-ES",show_all=True)
                    posibilidades=posibilidades['alternative']

                    for x in range(0,4): #ciclo para guardar en @español las posibilidades del reconocimiento de voz
                        try:

                            español['text'].append({
                                  str(x): posibilidades[x]['transcript']
                                })
                        except:
                            pass
                    #reconocer voz ingles
                    text = r.recognize_google(audio,language = "en-US");
                    posibilidades = r.recognize_google(audio,language = "en-US",show_all=True)
                    posibilidades=posibilidades['alternative']
                    ingles['text'] = []
                    for x in range(0,4):#ciclo para guardar en @ingles las posibilidades del reconocimiento de voz
                        try:
                            ingles['text'].append({
                                  str(x): posibilidades[x]['transcript']
                                })
                        except:
                            pass
                    lang=self.DeterminarLenguaje(ingles['text'],español['text']);
                    tts={}
                    tts['lang']=[lang]

                    #guardar el lenguaje que se hablo, esto para que el tts
                    #Sepa en que lenguaje responder
                    with open('lang.json', 'w+') as outfile:
                        json.dump(tts, outfile)

                    if lang == "esp":
                        traduct=self.traducir(español['text'])
                        jason['text']=traduct

                    else:
                        jason['text'] = ingles

                    #Guardar json
                    with open('data.json', 'w+') as outfile:
                        json.dump(jason, outfile)

                    #cargar el json guardado
                    with open('data.json') as json_file:
                        data = json.load(json_file)

                    #se imprime el json
                        print(data)
                except Exception as e: print(e)
Tts()
