# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 13:44:07 2019

@author: reinaqu
"""
import random
from cartas import *

PARTIDOS = ["Ciudadanos","PP", "PSOE", "Unidas Podemos","Vox"]

def mostrar_enumerado (iterable):
    for indx, elem in enumerate(iterable,1):
        print(f"{indx}-{elem}")
        
def generar_votos_aleatorios(num=10):
    lista = [ ]
    for _ in range(num):
        partido = random.choice(PARTIDOS)
        lista.append(partido)
    return lista

#Versión con definición por compresión
def generar_votos_aleatorios2(num=10):
    return [random.choice(PARTIDOS)for _ in range(num)]
if __name__ == '__main__':
    votos = generar_votos_aleatorios(20)
    mostrar_enumerado(votos)
  