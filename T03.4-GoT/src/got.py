from collections import *
import csv
from parsers import *


BatallaGOT = namedtuple('BatallaGOT', 'nombre, rey_atacante, rey_atacado, gana_atacante, muertes_principales, comandantes_atacantes, comandantes_atacados, region, num_atacantes, num_atacados')

def lee_batallas(fichero):
    with open(fichero, encoding="utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        res = []
        for nombre, rey_atacante, rey_atacado, gana_atacante, muertes_principales, comandantes_atacantes, comandantes_atacados, region, num_atacantes, num_atacados in lector:
            gana_atacante = parse_bool(gana_atacante)
            muertes_principales = parse_bool(muertes_principales)
            comandantes_atacados = parsea_comandantes(comandantes_atacados)
            comandantes_atacantes = parsea_comandantes(comandantes_atacantes)
            num_atacantes = parse_int(num_atacantes)
            num_atacados = parse_int(num_atacados)
            res.append(BatallaGOT(nombre, rey_atacante, rey_atacado, gana_atacante, muertes_principales, comandantes_atacantes, comandantes_atacados, region, num_atacantes, num_atacados))
        return res

def reyes_mayor_menor_ejercito(batallas):
    res = acumular_ejercitos_por_rey(batallas)
    return (max(res, key=res.get), min(res, key=res.get))

def acumular_ejercitos_por_rey(batallas):
    res = {}
    for b in batallas:
        guardar_dict(res, b.rey_atacante, b.num_atacantes)
        guardar_dict(res, b.rey_atacado, b.num_atacados)
    return res

def guardar_dict(dicc, rey, num_soldados):
    if num_soldados != None:
        if rey in dicc:
            dicc[rey] += num_soldados
        else:
            dicc[rey] = num_soldados


def batallas_mas_comandante(batallas, regiones=None, n=None):
    generador = ((b.nombre, len(b.comandantes_atacantes) + len(b.comandantes_atacados)) for b in batallas if regiones == None or b.region in regiones)
    res = sorted(generador, key=lambda it:it[1], reverse=True)
    if n != None:
        res = res[:n]
    return res

def rey_mas_victorias(batallas, rol="ambos"):
    reyes_ganadores = []
    for b in batallas:
        if (rol == "atacante" or rol == "ambos") and b.gana_atacante:
            reyes_ganadores.append(b.rey_atacante)
        if (rol == "atacado" or rol == "ambos") and b.gana_atacante:
            reyes_ganadores.append(b.rey_atacante)

    c = Counter(reyes_ganadores)
    res = None
    if len(c)>0:
        res = max(c, key=c.get)
        
    return res













