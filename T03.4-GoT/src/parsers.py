def parse_bool(cadena):
    if cadena.lower() == "win":
        cadena = True
    elif cadena.lower() == "lose":
        cadena = False
    elif cadena == "1":
        cadena = True
    elif cadena == "0":
        cadena = False
    else:
        cadena = None
    return cadena

def parsea_comandantes(cad):
    return [cad.strip() for cad in cad.split(",")]

def parse_int(n):
    if n == "":
        n = None
    else:
        return int(n)