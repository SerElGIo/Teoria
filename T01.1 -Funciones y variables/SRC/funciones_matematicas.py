from __future__ import division


def perimetro_rectangulo(base,altura):
    perimetro = 2*base + 2*altura
    return perimetro

def hipotenusa_triangulo(c1,c2):
    hipotenusa = (c1**2 + c2**2)**0.5
    return hipotenusa

def operaciones(n1,n2):
    suma = n1 + n2
    resta = n1 - n2
    multiplicacion = n1 * n2
    division = n1 / n2
    return suma, resta, multiplicacion, division

def temperatura(f,c):
    c = (f-32)*(5/9)
    return c

def media_tres(n1,n2,n3):
    media = (n1 + n2 + n3)//3
    return media 

def cambio_valor(valor1,valor2):
    x = valor1
    valor1 = valor2
    valor2 = x
    return valor1, valor2
    
def tiempo(minutos):
    horas = minutos//60
    minutos_resto = minutos%60
    return horas, minutos_resto
    
    