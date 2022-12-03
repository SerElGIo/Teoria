# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 13:43:19 2019

@author: reinaqu_2
"""

from collections import namedtuple
import statistics
Carta = namedtuple("Carta", "palo valor")

def crear_dicc_conteo_valores (cartas):
    '''
    Recibe:
    @param cartas: una lista de tuplas Carta(palo, valor)
    @type cartas: [Carta(str,int)]
    Devuelve:
    @return: Un diccionario que tiene como clave los valores de las cartas y como valores el número de cartas (frecuencia) con ese valor
    @rtype: {int:int}
    '''
    res = dict() # clave = valor de la carta
    for carta in cartas:
        clave = carta.valor
        if carta.valor in res: #La clave ya esta en el diccionario
            res[clave] = res[clave] + 1
        else:
            res[clave] = 1
    return res

def crear_dicc_valores_por_palos (cartas):
    '''
    Recibe:
    @param cartas: una lista de tuplas Carta(palo, valor)
    @type cartas: [Carta(str,int)]
    Devuelve:
    @return: Un diccionario que tiene como clave los palos y como valores una lista con los valores de las cartas de ese palo
    @rtype: {str:[int]}
    '''
    res = dict() # clave = valor de la carta
    for carta in cartas:
        clave = carta.palo
        if clave in res: #El palo ya esta en el diccionario
            res[clave].append(carta.valor)
        else:
            res[clave] = [carta.valor]
    return res

def crear_dicc_valores_por_palos2(cartas):
    '''
    Recibe:
    @param cartas: una lista de tuplas Carta(palo, valor)
    @type cartas: [Carta(str,int)]
    Devuelve:
    @return: Un diccionario que tiene como clave los palos y como valores una lista con los valores de las cartas de ese palo
    @rtype: {str:[int]}
    '''
    res = dict() # clave = valor de la carta
    for carta in cartas:
        clave = carta.palo
        if clave in res: #El palo ya esta en el diccionario
            res[clave].add(carta.valor)
        else:
            res[clave] = {carta.valor}
    return res
    


def obtener_clave_mayor(dicc):
    '''
    Recibe:
    @param dicc: Un diccionario que tiene como clave los valores de las cartas y como valores el número de cartas con ese valor
    @type: {int:int}       
    Devuelve:
    @return: La clave con valor mayor, según el orden natural
    @rtype: int
    '''
    return max(dicc)

def obtener_valor_mayor_frecuencia(dicc):
    '''
    Recibe:
    @param dicc: Un diccionario que tiene como clave los valores de las cartas y como valores el número de cartas con ese valor
    @type: {int:int}
    Devuelve:
    @return: El valor mayor, que en ese caso es el valor de carta con una frecuencia mayor
    @rtype: int
    '''
    return max(dicc, key=dicc.get)

def obtener_media_valores_por_palos(cartas):
    '''
    Recibe:
    @param cartas: una lista de tuplas Carta(palo, valor)
    @type cartas: [Carta(str,int)]
    Devuelve:
    @return: Un diccionario en el que la clave son los palos y los valores, la media de los valores de las cartas de ese palo
    @rtype: {str:float} 
    '''
    res = dict() # clave = valor de la carta
    for carta in cartas:
        clave = carta.palo
        if clave in res: #El palo ya esta en el diccionario
            res[clave].append(carta.valor)
        else:
            res[clave] = [carta.valor]
    return {palo:statistics.mean(lista_valores) for palo, lista_valores in res.items()}


def obtener_max_valores_por_palos(cartas):
    '''
    Recibe:
    @param cartas: una lista de tuplas Carta(palo, valor)
    @type cartas: [Carta(str,int)]       
    Devuelve:
    @return: Un diccionario en el que la clave son los palos y los valores, el mayor valor de una carta de ese palo
    @rtype: {str: int}
    '''
    res = dict() # clave = valor de la carta
    for carta in cartas:
        clave = carta.palo
        if clave in res: #El palo ya esta en el diccionario
            res[clave].add(carta.valor)
        else:
            res[clave] = {carta.valor}
    return {palo:max(conj_valores) for palo, conj_valores in res.items()}