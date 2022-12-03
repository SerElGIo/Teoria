from imc import *


#tupla_persona = lee_datos_persona()
#print(tupla_persona)
#print(f"{tupla_persona[0]} tu peso es {tupla_persona[1]} kg y tu estatura es {tupla_persona[2]} m ")
#mostrar_estado_nutricional(tupla_persona)
'''
lista_personas = lee_personas(4)
for tupla_persona in lista_personas:
    mostrar_estado_nutricional(tupla_persona)
'''

lista_personas = lee_fichero_personas2("data/personas.csv")
for tupla_persona in lista_personas:
    mostrar_estado_nutricional(tupla_persona)