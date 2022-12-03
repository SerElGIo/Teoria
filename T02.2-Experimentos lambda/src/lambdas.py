from turtle import tracer

from funciones import cuadrados, iniciales_mayuscula


def transforma(lista,funcion_transformacion):
    '''
    @param lista: Lista de elementos
    @type lista:[any]
    @param funcion_transformacion: Funcion que se le aplica a un elemento de la lista para transformarlo en otro
    @type funcion_transformacion:
    @return: listamcon los cuadrados de los números de la liosta general
    @rtype:[R]
    '''
    lista_transformada = []
    for elem in lista:
        lista_transformada.append(funcion_transformacion(elem))
    return lista_transformada

def cuadrado(elem):
    return elem**2

def cubo(elem):
    return elem**3

def es_par(elem):
    return elem%2 == 0

def inicial_mayuscula(elem):
    return elem[0].upper()

if __name__ == '__main__':
    print(transforma([1,2,3,4],lambda elem:elem**2))
    print(transforma([1,2,3,4], lambda elem:elem**3))
    print(transforma([1,2,3,4], lambda elem:elem%2 == 0))
    print(transforma(['java', 'python', 'c', 'R'], lambda elem:elem[0].upper()))
    print(transforma(['java', 'python', 'c', 'R'], len))





