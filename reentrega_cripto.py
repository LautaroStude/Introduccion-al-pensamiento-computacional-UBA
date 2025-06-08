def leer_archivo(nombre):
    with open(nombre, "r", encoding="utf-8") as archivo:
        texto = archivo.read()

    return texto

def obtener_indice(caracter,cadena):
    i = 0
    while not caracter == cadena[i]:
        i += 1
    return i
            
def codificar_caracter(letra, alfabeto, k):    
    posicion = obtener_indice(letra, alfabeto)
    cifrado = alfabeto[(posicion + k) % len(alfabeto)]
    
    return cifrado
    
def normalizar(mensaje):
    nuevo_mensaje = ""
    i = 0
    while i < len(mensaje):
        if mensaje[i] == "á":
            nuevo_mensaje = nuevo_mensaje + "a"
        
        elif mensaje[i] == "é":
            nuevo_mensaje = nuevo_mensaje + "e"
        
        elif mensaje[i] == "í":
            nuevo_mensaje = nuevo_mensaje + "i"
            
        elif mensaje[i] == "ó":
            nuevo_mensaje = nuevo_mensaje + "o"
            
        elif mensaje[i] == "ú":
            nuevo_mensaje = nuevo_mensaje + "u"
            
        elif mensaje[i] == "ü":
            nuevo_mensaje = nuevo_mensaje + "u"
        else:  
            nuevo_mensaje = nuevo_mensaje + mensaje[i]
        i = i + 1
        
    return nuevo_mensaje.lower()

def codificar(mensaje, alfabeto, k):
    mensaje = normalizar(mensaje)
    codificado = ""
    i = 0
    
    while i < len(mensaje):
        if mensaje[i] in alfabeto:
            codificado = codificado + codificar_caracter(mensaje[i], alfabeto, k)
        else:
            codificado = codificado + mensaje[i]
        i = i + 1
    return codificado         

def decodificar_caracter(letra, alfabeto, k):
    posicion = obtener_indice(letra, alfabeto)
    descifrado = alfabeto[(posicion - k) % len(alfabeto)]
    
    return descifrado
    
def decodificar(mensaje, alfabeto, k):
    mensaje = normalizar(mensaje)
    decodificado = ""
    i = 0
    
    while i < len(mensaje):
        if mensaje[i] in alfabeto:
            decodificado = decodificado + decodificar_caracter(mensaje[i], alfabeto, k)
        else:
            decodificado = decodificado + mensaje[i]
        i = i + 1
    return decodificado

def codificar_archivo(nombre, alfabeto, k):
    contenido = leer_archivo(nombre)
    resultado = codificar(contenido, alfabeto, k)
    nuevo_nombre = nombre.rsplit(".", 1)[0] + ".enc"
    with open(nuevo_nombre, "w", encoding="utf-8") as archivo:
        archivo.write(resultado)
    return resultado

def decodificar_archivo(nombre, alfabeto, k):
    contenido = leer_archivo(nombre)
    resultado = decodificar(contenido, alfabeto, k)
    nuevo_nombre = nombre.rsplit(".", 1)[0] + ".dec"
    with open(nuevo_nombre, "w", encoding="utf-8") as archivo:
        archivo.write(resultado)
    return resultado

def quitar(caracteres, cadena):
    resultado = ""
    for letra in cadena:
        if letra not in caracteres:
            resultado = resultado + letra
    return resultado

def sin_repetidos(cadena):
    cadena = cadena.lower()
    resultado = ""
    for c in cadena:
        if c not in resultado:
            resultado += c
    return resultado

def crear_codificacion(palabra, alfabeto):
    palabra_sin_repes = sin_repetidos(palabra)
    resto_alfabeto = quitar(palabra_sin_repes, alfabeto)
    cifrado = palabra_sin_repes + resto_alfabeto
    diccionario = {}
    for in in range(len(alfabeto)):
        diccionario[alfabeto[i]] = cifrado[i]
    return diccionario 

