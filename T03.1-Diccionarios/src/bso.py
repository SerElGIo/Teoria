# -*- coding: utf-8 -*-
'''
Created on 7 nov. 2018

@author: reinaqu
'''
def crear_dicc_titulos_anyos(bsos):
    '''
    Recibe:
    @param bsos: una lista de tuplas (titulo, año)
    @type: [(str, int)]
    Devuelve:
    @return: Un diccionario que tiene como clave los títulos y como valores los años
    @rtype: {str:int}
    '''
    besos = dict() # clave = valor de la carta
    for bsoclave, bsovalor in bsos:
        besos[bsoclave] = bsovalor        
    return besos

def crear_dicc_titulos_anyos2(bsos):
    '''
    Recibe:
    @param bsos: una lista de tuplas (titulo, año)
    @type: [(str, int)]
    Devuelve:
    @return: Un diccionario que tiene como clave los títulos y como valores los años
    @rtype: {str:int}
    '''
    return {titulo: anyo for titulo, anyo in bsos}

def crear_dicc_anyos_conteo_titulos (bsos):
    '''
    Recibe:
    @param bsos: una lista de tuplas (titulo, año)
    @type: [(str, int)]
    Devuelve:
    @return: Un diccionario que tiene como clave los años y como valores el número de títulos
          de ese año
    @rtype: {int:int}
    '''
    pass

def crear_dicc_anyos_lista_titulos (bsos):
    '''
    Recibe:
    @param bsos: una lista de tuplas (titulo, año)
    @type: [(str, int)]
    Devuelve:
    @return: Un diccionario que tiene como clave los años y como valores una lista con los títulos
          de ese año
    @rtype:{int:[str]}
    '''
    pass

def obtener_clave_mayor(dicc_bso):
    '''
    Recibe:
    @param dicc_bso: Un diccionario que tiene como clave los títulos y como valores los años
    @type: {str:int}
    Devuelve:
    @return: La clave con valor mayor, segun el orden natural
    @rtype: str
    '''
    pass

def obtener_valor_mayor(dicc_bso):
    '''
    Recibe:
    @param dicc_bso: Un diccionario que tiene como clave los títulos y como valores los años
    @type: {str:int}
    Devuelve:
    @return: El valor mayor, que en este caso es el año más reciente.
    @rtype: int
    '''
    pass

def obtener_nombre_mas_largo(dicc_bso):
    '''
    Recibe:
    @param dicc_bso: Un diccionario que tiene como clave los títulos y como valores los años
    @type: {str:int}
    Devuelve:
    @return: El valor mayor, que en este caso es el año más reciente
    @rtype: int
    '''
    pass