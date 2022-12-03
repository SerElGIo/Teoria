# -*- coding: utf-8 -*-
'''
Created on 7 nov. 2018

@author: reinaqu
'''
from programadores import *
import random

PROGRAMADORES = ["Frances E. Allen", "Stephanie Shirley", "Grace Hopper",
                 "James Gosling", "Evelyn Berezin", "Margaret Hamilton",
                 "Guido Van Rossum", "Mary Allen", "Dennis Ritchie"]

LENGUAJES = ["Java", "C", "Python", "C++", "R", "Javascript", "COBOL", "ADA",
             "LISP", "Prolog", "Visual Basic", "C#"]    

def mostrar_numerado(iterable):
    for indx, elem in enumerate(iterable, 1):
        print(f"{indx}-{elem}")
        
def generar_lenguajes_aleatorios (lenguajes):
    '''
    @param lenguajes: Lista con los nombres de los lenguajes de programación
    @type lenguajes: [str]
    '''
    #genero el número de lenguajes del conjunto resultado
    num_lenguajes = random.randint(1,len(lenguajes))
    return {random.choice(lenguajes) for _ in range(num_lenguajes)}

def generar_programadores (programadores, lenguajes):    
    '''
    @param programadores: Lista con los nombres de los programadores
    @type programadores: [str]
    @param lenguajes: Lista con los nombres de los lenguajes de programación
    @type lenguajes: [str]
    '''
    return [Programador(nombre, generar_lenguajes_aleatorios(lenguajes)) \
                for nombre in programadores]
    

def test_programador_conoce_lenguaje(programador, lenguaje):
    print(f"¿Conoce el programador{programador.nombre} el lenguaje {lenguaje}?")
    print(programador_conoce_lenguaje(programador, lenguaje))

def test_lenguajes_comunes(programador1, programador2):
    print(f"Son {programador1.nombre} y {programador2.nombre} en el mismo lenguaje?")
    print(lenguajes_comunes(programador1.nombre, programador2.nombre ))


def main():
    programadores = generar_programadores(PROGRAMADORES, LENGUAJES)
    print ("Se han generado las siguientes programadores")
    mostrar_numerado(programadores) 
    ## Test Ejercicio 1
    test_programador_conoce_lenguaje(programadores[0], "java" )
    test_programador_conoce_lenguaje(programadores[0], "python" )
    ## test ejercico 2


    ## test ejercicio 3
    test_lenguajes_comunes(programadores[0],programadores[2])
    
    
if __name__=="__main__":
    main()  