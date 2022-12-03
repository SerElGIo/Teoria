from entrada import *
import csv
"""
Modulo para trabajar con el indice de masa corporal 
Segundo proyecto de FP
"""

def lee_datos_persona():
    """
    Lee el nombre, el peso y la estatura de una persona
    y devuelve una tupla con esos 3 datos.
    """
    nombre = input("Introduzca su nombre: ") #nombre es str
    peso = int(input("introduzca su peso (en kg): "))
    estatura = float(input("Introduzca su estatura (en m): "))
    return (nombre, peso, estatura)


def calcular_IMC(peso, estatura):
    """
    Dados peso(entero) y una estatura (real)
    Devuelve el indice de masa corporal
    responsabilidad unica: calcular
    """
    return round(peso/(estatura)**2,2)

def calcular_estado_nutricial(imc):
    """
    Dado el IMC devuelve una cadena que representa el estado nutricional
    """

    if imc <18.5:
        en =  "Bajo peso"
    elif imc < 25:
        en = "Normal"
    elif imc < 30:
        en = "Sobrepeso"
    else:
        en = "Obesidad"
    return en

def mostrar_estado_nutricional(tupla_persona):
    '''
    dada una tupla con los datos de una persona,
    muestra or la consola un mensaje con  su imc y su 
    estado nutricional
    '''

    imc = calcular_IMC(tupla_persona[1], tupla_persona[2])
    en = calcular_estado_nutricial(imc)
    print(f"{tupla_persona[0]} tu estado es {imc} y tu estado nutricional es {en}")
    
def lee_personas(n):
    '''
    Lee por teclado los datos de n personas y devuelve una lista de tuplas [(nombre, peso, estatura)] con los datos
    de las n personas
    '''
    res = []
    for i in range(n):
        print(f"Datos de la persona  {i+1}")
        tupla_persona = lee_datos_persona()
        res.append(tupla_persona)
    return res

def lee_fichero_personas(nombre_fichero):
    personas = []
    with open(nombre_fichero, encoding = "utf-8") as f:
        for linea in f:
            nombre, estatura, peso = linea.split(",")
            peso = int(peso)
            estatura = float(estatura)
            personas.append((nombre, peso, estatura))
        return personas

def lee_fichero_personas2(nombre_fichero):
    '''
    @param nombre_fichero: El nombre (y ruta) del fichero csv a leer.
    @typenombre_fichero: str
    @return:Una lista de tuplas con el nombre, peso, altura.
    @rtype: [(str,int,float)]
    '''
    personas = []
    with open(nombre_fichero, encoding = "utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        for nombre, estatura, peso in lector:
            estatura = float(estatura)
            peso = int(peso)
            personas.append((nombre, peso, estatura))
        return personas
