# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 13:44:07 2019

@author: reinaqu
"""
import random
from cartas import *

PALOS = ["Oros", "Copas","Espadas", "Bastos"]

def mostrar_dicc_por_linea(dicc):
    for clave, valor in dicc.items():
        print(clave, "==>", valor)

def generar_cartas_aleatorias(num=10):
    lista = [ ]
    for _ in range(num):
        palo = random.choice(PALOS)
        valor = random.randint(1,12)
        lista.append(Carta(palo, valor))
    return lista

#Versión con definición por compresión
def generar_cartas_aleatorias_2(num=10):
    return [Carta(random.choice(PALOS), random.randint(1,12))
               for _ in range(num)]
    
def test_crear_dicc_conteo_valores(cartas):
    print("test_crear_dicc_conteo_valores", "="*20)
    dicc = crear_dicc_conteo_valores(cartas)
    print(dicc)

def test_crear_dicc_valores_por_palos(cartas):
    print("test_obtener_valor_mayor_frecuencia", "="*20)
    dicc = crear_dicc_valores_por_palos2(cartas)
    mostrar_dicc_por_linea(dicc)
    
def test_obtener_clave_mayor(cartas):
    print("test_obtener_clave_mayor", "="*20)
    dicc = crear_dicc_conteo_valores(cartas)
    print(obtener_clave_mayor(dicc))
    
def test_obtener_valor_mayor_frecuencia(cartas):
    print("test_obtener_valor_mayor_frecuencia", "="*20)
    dicc = crear_dicc_conteo_valores(cartas)
    print(obtener_valor_mayor_frecuencia(dicc))
    
def test_obtener_media_valores_por_palos(cartas):
    print("test_obtener_media_valores_por_palos", "="*20)
    print(obtener_media_valores_por_palos(cartas))

def test_obtener_max_valores_por_palos(cartas):
    print("test_obtener_media_valores_por_palos", "="*20)
    print(obtener_max_valores_por_palos(cartas))
    
if __name__ == '__main__':
    MAZO1 = generar_cartas_aleatorias(2000)
    MAZO2 = generar_cartas_aleatorias(20)
    print(MAZO1)
    print(MAZO2)
    
    test_crear_dicc_conteo_valores (MAZO1)
    test_crear_dicc_conteo_valores (MAZO2)
    
    test_crear_dicc_valores_por_palos(MAZO1)
    test_crear_dicc_valores_por_palos(MAZO2)
    
    test_obtener_clave_mayor(MAZO1)
    test_obtener_clave_mayor(MAZO2)
    
    test_obtener_valor_mayor_frecuencia(MAZO1)
    test_obtener_valor_mayor_frecuencia(MAZO2)
    
    test_obtener_media_valores_por_palos(MAZO1)
    test_obtener_media_valores_por_palos(MAZO2)
    
    test_obtener_max_valores_por_palos(MAZO1)
    test_obtener_max_valores_por_palos(MAZO2)