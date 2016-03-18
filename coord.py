# -*- coding: utf-8 -*-

import json
import urllib2
import sys

def get_coord(local):
    url="http://maps.googleapis.com/maps/api/geocode/json?address="+str(local[1])
    j=json.load(urllib2.urlopen(url))
    try:
        print(str(j['results'][0]['geometry']['location']['lat'])+' '+str(j['results'][0]['geometry']['location']['lng']))
    except:
        print("Erro! Entrada não reconhecida.Tente novamente.")

def get_dist(start, finish, mode='car'):
    url="https://maps.googleapis.com/maps/api/distancematrix/json?origins="+str(start)+"&destinations="+str(finish)+"&mode="+str(mode)+"&language=pt-BR&key=AIzaSyCAGWSj9hWWv0n9DjcTcDLLIuYUQT0quSM"
    j=json.load(urllib2.urlopen(url))
    try:
        print (j['rows'][0]['elements'][0]['distance']['text']+' - '+j['rows'][0]['elements'][0]['duration']['text'])
    except:
        print("Erro! Entradas não reconhecidas.Tente novamente.")



if len(sys.argv)==2 :
    get_coord(sys.argv)
else:
    if len(sys.argv)==3:
        get_dist(sys.argv[1],sys.argv[2])
    else:
        if len(sys.argv)==4:
            get_dist(sys.argv[1],sys.argv[2],sys.argv[3])
        else:
            print("Dados inválidos.\nEntre uma das opções:\n1-Entre o nome de uma cidade para retornar suas coordenadas (lat, long)\n2-Entre os nomes de 2 cidades para cálculo da distância entre elas\n3-Entre, além dos nomes, o tipo do transporte (car,bicycling,walking)")

