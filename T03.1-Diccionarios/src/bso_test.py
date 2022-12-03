# -*- coding: utf-8 -*-
'''
Created on 7 nov. 2018

@author: reinaqu
'''
from bso import *

def test_crear_dicc_titulos_anyos (bso):
    print("1. Cree un diccionario que tenga como claves los títulos y como valores los años")
    dicc = crear_dicc_titulos_anyos (bso)
    print(dicc)

def test_crear_dicc_anyos_conteo_titulos (bso):
    print("2. Cree un diccionario que tenga como claves los años y como valores el número de títulos de ese año")
    dicc = crear_dicc_anyos_conteo_titulos (bso)
    print(dicc)

def test_crear_dicc_anyos_lista_titulos (bso):
    print("3. Cree un diccionario que tenga como claves los años y como valores una lista con los títulos de ese año")
    dicc = crear_dicc_anyos_lista_titulos (bso)
    print(dicc)
    
def test_obtener_clave_mayor(bso):
    print("4. Dado un diccionario de titulos y años, devuelva el título mayor")
    dicc = crear_dicc_titulos_anyos (bso)
    mayor = obtener_clave_mayor(dicc)
    print(mayor)    
              
def test_obtener_valor_mayor(bso):
    print("5. Dado un diccionario de titulos y años, devuelva el año mayor")
    dicc = crear_dicc_titulos_anyos (bso)
    mayor = obtener_valor_mayor(dicc)
    print(mayor)    

def test_obtener_titulo_mas_largo(bso):
    print("6. Dado un diccionario de titulos y años, devuelva el título con más caracteres")
    dicc = crear_dicc_titulos_anyos (bso)
    mayor = obtener_nombre_mas_largo(dicc)
    print(mayor)
        
if __name__ == '__main__':
    L_BSO = {("Thriller",1982), 
             ("Back in Black",1980), 
             ("The Dark Side of the Moon", 1973), 
             ("The Bodyguard",1992), 
             ("Bat Out of Hell",1977), 
             ("Their Greatest Hits (1971-1975)", 1976), 
             ("Saturday Night Fever",1977), 
             ("Rumours",1977)}
    print(L_BSO)
    test_crear_dicc_titulos_anyos(L_BSO)
    test_crear_dicc_anyos_conteo_titulos (L_BSO)
    test_crear_dicc_anyos_lista_titulos (L_BSO)
    test_obtener_clave_mayor(L_BSO)
    test_obtener_valor_mayor(L_BSO)
    test_obtener_titulo_mas_largo(L_BSO)