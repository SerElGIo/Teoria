import csv
from matplotlib import pyplot as plt

def lee_audiencias(fichero):
    ''' Lee el fichero de entrada y devuelve una lista de audiencias
    
    ENTRADA: 
       @param fichero: nombre del fichero
       @type fichero:  str
    SALIDA: 
       @return: lista de audiencias
       @rtype: [(int, float)] 

    Cada línea del fichero se corresponde con la audiencia de un programa,
    y se representa con una tupla con los siguientes valores:
        - edición
        - audiencia
    Hay que transformar la entrada (cadenas de caracteres) en valores numéricos
    para que puedan ser procesados posteriormente.
    '''
    audiencias=[]
    with open(fichero, encoding='utf-8') as f:
        # Se crea un objeto lector (un iterator) que separará los valores por comas 
        lector = csv.reader(f)
        for edicion, share in lector:
            edicion = int(edicion)
            share = float(share)
            audiencias.append((edicion, share))
    return audiencias

def lee_audiencias2(fichero):
    ''' Lee el fichero de entrada y devuelve una lista de audiencias
    
    ENTRADA: 
       @param fichero: nombre del fichero
       @type fichero:  str
    SALIDA: 
       @return: lista de audiencias
       @rtype: [(int, float)] 

    Cada línea del fichero se corresponde con la audiencia de un programa,
    y se representa con una tupla con los siguientes valores:
        - edición
        - audiencia
    Hay que transformar la entrada (cadenas de caracteres) en valores numéricos
    para que puedan ser procesados posteriormente.
    Solución utilizando una definición de audiencias por compresión
    '''
    with open(fichero, encoding='utf-8') as f:
        # Se crea un objeto lector (un iterator) que separará los valores por comas 
        lector = csv.reader(f)
        # Lista por comprensión sobre el objeto lector
        audiencias = [(int(edicion), float(share)) for edicion, share in lector]
    return audiencias

def calcula_ediciones(audiencias):
    ''' Calcula el conjunto de ediciones presentes en una lista de audiencias
    
    ENTRADA: 
       @param audiencias: lista de tuplas de audiencias
       @type audiencias: [(int, float)]
    SALIDA: 
       @return: El número de ediciones del programa
       @rtype: int 

    Toma como entrada una lista de tuplas (edición, share) y produce como
    salida el número de ediciones del programa
    '''
    # Calculamos el conjunto de ediciones presentes
    ediciones = set()
    for edicion, _ in audiencias:
        ediciones.add(edicion)
    # Devolvemos el tamaño del conunto
    return len(ediciones)

def calcula_ediciones2(audiencias):
    ''' Calcula el conjunto de ediciones presentes en una lista de audiencias
    
    ENTRADA: 
       @param audiencias: lista de tuplas de audiencias
       @type audiencias: [(int, float)]
    SALIDA: 
       @return: El número de ediciones del programa
       @rtype: int 

    Toma como entrada una lista de tuplas (edición, share) y produce como
    salida el número de ediciones del programa
    Solución utilizando una definición de audiencias por compresión
    '''
    # Calculamos el conjunto de ediciones presentes
    ediciones = {e for e, _ in audiencias}
    # Devolvemos el tamaño del conunto
    return len(ediciones)


def filtra_por_ediciones(audiencias, ediciones):
    ''' Selecciona las tuplas correspondientes a unas determinadas ediciones
    
    ENTRADA: 
       @param audiencias: lista de audiencias 
       @type audiencias: [(int, float)]
       @param ediciones: lista de ediciones a seleccionar 
       @type ediciones: [int]
    SALIDA:
       @return: lista de tuplas de audiencias seleccionadas
       @rtype:  [(int, float)]

    Toma como entrada una lista de tuplas (edición, share) y un conjunto de 
    ediciones. Produce como salida otra lista de tuplas en la que solo se
    incluyen aquellas cuya edición sea una de las que se reciben como parámetro.
    '''
    filtradas = []
    for edicion, share in audiencias:
        if edicion in ediciones:
            filtradas.append((edicion, share))
    return filtradas


def filtra_por_ediciones2(audiencias, ediciones):
    ''' Selecciona las tuplas correspondientes a unas determinadas ediciones
    
    ENTRADA: 
       @param audiencias: lista de audiencias 
       @type audiencias: [(int, float)]
       @param ediciones: lista de ediciones a seleccionar 
       @type ediciones: [int]
    SALIDA:
       @return: lista de tuplas de audiencias seleccionadas
       @rtype:  [(int, float)]

    Toma como entrada una lista de tuplas (edición, share) y un conjunto de 
    ediciones. Produce como salida otra lista de tuplas en la que solo se
    incluyen aquellas cuya edición sea una de las que se reciben como parámetro.
    '''
    filtradas = [(edicion, share) for edicion, share in audiencias if edicion in ediciones]
    return filtradas

def agrupa_por_ediciones(audiencias):
    '''Función auxiliar

    :param audiencias: lista de tuplas (edicion, share) con las audiencias de un programa de televisión
    :type audiencias: [(int, float)]
    :return: Un diccionario en el que las claves son las ediciones y los valores la lista de shares de esa edición
    :rtype: {int:[float]}
    '''
    res = dict() # Crea diccionario vacío
    # Vamos recorriendo las audiencias
    for edicion, share in audiencias:
        if edicion in res: # Si la edición ya está en el diccionario
            res[edicion].append(share)  # Se añade el share a la lista de shares que ya hay de esa edición
        else: # Si la edición no está en el diccionario
            res[edicion] = [share]  # Se añade una nueva pareja al diccionario para la edición y una lista con el share
    return res


def medias_por_ediciones(audiencias):
    ''' Calcula la media de audiencia para cada edición
    
    ENTRADA: 
       @param audiencias: lista de audiencias 
       @type audiencias: [(int, float)]
    SALIDA:
       @return: medias de audiencia por cada edición
       @rtype: {int: float}

    Toma como entrada una lista de tuplas (edición, share) y produce como
    salida un diccionario en el que las claves son las ediciones y los
    valores son las medias de audiencia de cada edición.
    '''
    medias = dict()
    d = agrupa_por_ediciones(audiencias)
    # Se recorre el diccionario d por parejas de elementos
    for edicion, lista_shares in d.items():
        # Usamos la lista de shares para calcular la media
        medias[edicion] = sum(lista_shares) / len(lista_shares)
    return medias


def muestra_evolucion_audiencias(audiencias, nombre_programa):
    ''' Genera una curva con la evolución de las audiencias
    
    ENTRADA: 
       @param audiencias: lista de audiencias
       @type audiencias: [(int, float)]
       @param nombre_programa: Nombre del programa
       @type nombre_programa: str

    SALIDA EN PANTALLA:
       - gráfica con la evolución de los shares a lo largo del tiempo

    Toma como entrada una lista de tuplas (edición, share) y muestra una
    curva con la evolución de los shares a lo largo del tiempo.
    
    Para generar la gráfica usaremos elementos del paquete matplotlib. Estas
    son las instrucciones que permiten trazar una curva a partir de la lista de
    shares:
        plt.plot(shares, label='audiencia')
        plt.legend()
        plt.show()
    '''
    # Calculamos la lista de shares
    shares = []
    for _, share in audiencias:
        shares.append(share)
    
    # Componemos y visualizamos la gráfica
    plt.title(f"Evolución de audiencias del programa {nombre_programa}")
    plt.xlabel("emisiones")
    plt.ylabel("shares")
    plt.plot(shares, label='audiencia')
    plt.legend()
    plt.show()


def muestra_evolucion_audiencias2(audiencias, nombre_programa):
    ''' Genera una curva con la evolución de las audiencias
    
    ENTRADA: 
       @param audiencias: lista de audiencias
       @type audiencias: [(int, float)]
       @param nombre_programa: Nombre del programa
       @type nombre_programa: str
    SALIDA EN PANTALLA:
       - gráfica con la evolución de los shares a lo largo del tiempo

    Toma como entrada una lista de tuplas (edición, share) y muestra una
    curva con la evolución de los shares a lo largo del tiempo.
    
    Para generar la gráfica usaremos elementos del paquete matplotlib. Estas
    son las instrucciones que permiten trazar una curva a partir de la lista de
    shares:
        plt.plot(shares, label='audiencia')
        plt.legend()
        plt.show()
    Solución con definición por compresión
    '''
    # Calculamos la lista de shares
    shares = [share for _, share in audiencias]
    
    # Componemos y visualizamos la gráfica
    plt.title(f"Evolución de audiencias del programa {nombre_programa}")
    plt.xlabel("emisiones")
    plt.ylabel("shares")
    plt.plot(shares, label='audiencia')
    plt.legend()
    plt.show()

def muestra_medias_por_ediciones(audiencias, nombre_programa):
    ''' Genera un diagrama de barras con la media de audiencia de cada edición
    
    ENTRADA: 
       @param audiencias: lista de audiencias
       @type audiencias: [(int, float)]
    SALIDA EN PANTALLA:
       - gráfica con las medias por cada edición

    Toma como entrada una lista de tuplas (edición, share) y muestra un diagrama
    de barras. Habrá una barra por cada edición presente en la lista de audiencias.
    Se mostrará la media de shares de cada edición.
    
    Estas son las instrucciones 'matplotlib' para trazar el diagrama de barras
    a partir de una lista de ediciones y otra lista (con el mismo orden) de
    medias de shares:
        plt.bar(ediciones, lista_medias)
        plt.xticks(ediciones, ediciones, fontsize=8)
        plt.show()
    '''
    
    # Calculamos las medias por cada edición
    dicc_medias = medias_por_ediciones(audiencias)
    # Calculamos la lista de ediciones
    ediciones = sorted(dicc_medias.keys())
    # Generamos una lista de medias con el mismo orden que las ediciones
    lista_medias = []
    for edicion in ediciones:
        lista_medias.append(dicc_medias[edicion])
    
    plt.title(f"Medias de shares por edición del programa {nombre_programa}")
    plt.xlabel("ediciones")
    plt.ylabel("medias")

    # Componemos y visualizamos la gráfica
    plt.bar(ediciones, lista_medias)
    plt.xticks(ediciones, ediciones, fontsize=8)
    plt.show()

def muestra_medias_por_ediciones2(audiencias, nombre_programa):
    ''' Genera un diagrama de barras con la media de audiencia de cada edición
    
    ENTRADA: 
       @param audiencias: lista de audiencias
       @type audiencias: [(int, float)]
    SALIDA EN PANTALLA:
       - gráfica con las medias por cada edición

    Toma como entrada una lista de tuplas (edición, share) y muestra un diagrama
    de barras. Habrá una barra por cada edición presente en la lista de audiencias.
    Se mostrará la media de shares de cada edición.
    
    Estas son las instrucciones 'matplotlib' para trazar el diagrama de barras
    a partir de una lista de ediciones y otra lista (con el mismo orden) de
    medias de shares:
        plt.bar(ediciones, lista_medias)
        plt.xticks(ediciones, ediciones, fontsize=8)
        plt.show()

    Solución con versiones por compresión
    '''
    
    # Calculamos las medias por cada edición
    dicc_medias = medias_por_ediciones(audiencias)
    # Calculamos la lista de ediciones
    ediciones = sorted(dicc_medias.keys())
    # Generamos una lista de medias con el mismo orden que las ediciones
    lista_medias = [dicc_medias[edicion] for edicion in ediciones]

    plt.title(f"Medias de shares por edición del programa {nombre_programa}")
    plt.xlabel("ediciones")
    plt.ylabel("medias")

    # Componemos y visualizamos la gráfica
    plt.bar(ediciones, lista_medias)
    plt.xticks(ediciones, ediciones, fontsize=8)
    plt.show()