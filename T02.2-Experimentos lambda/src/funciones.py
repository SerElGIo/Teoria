# -*- coding: utf-8 -*-
'''
Created on 9 nov 2021

@author: reinaqu_2
'''
def cuadrados(lista):
    '''
    @param lista: lista de números
    @type lista :[int/float]
    @return: lista con los cuadrados de los números
    de la lista original
    @rtype: [int/float]
    '''
    lista_transformada = []
    for elem in lista:
        lista_transformada.append(elem**2)
    return lista_transformada

def cubos(lista):
    '''
    @param lista: lista de números
    @type lista :[int/float]
    @return: lista con los cubos de los números
    de la lista original
    @rtype: [int/float]
    '''
    lista_transformada = []
    for elem in lista:
        lista_transformada.append(elem**3)
    return lista_transformada

def lista_son_pares(lista):
    '''
    @param lista: lista de números
    @type lista :[int/float]
    @return: lista con booleanos. El booleano será True si el número de la lista
    original es par y False en caso contrario
    de la lista original
    @rtype: [bool]
    '''
    lista_transformada = []
    for elem in lista:
        lista_transformada.append(elem%2 == 0)
    return lista_transformada

def iniciales_mayuscula(lista):
    '''
    @param lista: lista de cadenas de caracteres
    @type lista :[str]
    @return: lista son cadenas de caracteres de un solo caracter, y ese caracter se
    corresponderá con la inicial de la cadena original en mayusculas
    de la lista original
    @rtype: [bool]
    '''
    lista_transformada = []
    for elem in lista:
        lista_transformada.append(elem[0].upper())
    return lista_transformada

if __name__ == '__main__':
    print(cuadrados([1,2,3,4]))
    print(cubos([1,2,3,4]))
    print(lista_son_pares([1,2,3,4]))
    print(iniciales_mayuscula(['java', 'python', 'c', 'R']))
    print(type(iniciales_mayuscula))






