# -*- coding: utf-8 -*-
'''
Created on 7 nov. 2018

@author: reinaqu
'''

from collections import namedtuple

Programador = namedtuple("Programador","nombre, leng_programacion")

# 1. Implementa una función que dados dado un programador y un lenguaje,
# devuelva cierto si ese programador conoce ese lenguaje.
def programador_conoce_lenguaje(programador, lenguaje):
    '''
    :param progrmador: tupla Programador
    :type programador: Programador(str, {str})
    :param lenguaje: nombre del lenguaje de programacion
    :type lenguaje: str
    '''
    return lenguaje in programador.leng_programacion

# 2. Implementa una función que dados dado un programador y un conjunto de lenguajes, devuelva cierto si ese programador conoce todos esos lenguajes.
def programador_conoce_lenguajes(programador, lenguajes):
    '''
    :param progrmador: tupla Programador
    :type programador: Programador(str, {str})
    :param lenguaje: un conjunto de lenguajes
    :type lenguaje: {str}
    '''
    return lenguajes <= programador.leng_programcion


# 3. Implementa una función que dados dos programadores, devuelva un conjunto con los lenguajes de programación en los que los dos programadores son expertos.
def lenguajes_comunes(programador1, programador2):
    return (programador1.leng_programcion & programador2.leng_programcion)

# 4. Implementa una función que dados dos programadores, devuelva un conjunto con todos los lenguajes de programación que conocen los dos 
# programadores.

# 5. Implementa una función que dados dos programadores, devuelva los lenguajes que solo conocen uno de los dos programadores.

# 6. Implementa una función que dados dos programadores, devuelva los lenguajes que conoce el primer programador y no el segundo.

# 7. Implementa una función que dados tres programadores, devuelva 
# los lenguajes que conocen el primero y el segundo y no conoce el tercero.