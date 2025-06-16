import random
import numpy as np
import matplotlib.pyplot as plt

#-> bosque con n celdas lineales/pueden tener un arbol o nada
#-> dif etapas, brotes, caida de rayos, propagacion de incendios, limpieza
#-> propagacion, ¿Hay brote donde cayo?
#-> todo lo anterior es un año

def generar_bosque(n):
    bosque = np.repeat([0], n)
    
    return bosque

#bosque = generar_bosque(10)

def cuantos(bosque, tipo_celda):
    i = 0
    contador = 0
    while i < len(bosque):
       if bosque[i] == tipo_celda:
           contador = contador + 1
       i = i + 1
    return contador 
        
def suceso_aleatorio(p):
    azar = random.randint(0, 100)
    probabilidad = False
    if azar <= p:
        probabilidad = True
    return probabilidad

def brotes(bosque, p):
    i = 0 
    while i < len(bosque):
        if bosque[i] == 0:
            if suceso_aleatorio(p) == True:
                bosque[i] = 1
        i = i + 1
    return bosque

#bosque = brotes(bosque, 80)

def rayos(bosque, f):
    i = 0 
    while i < len(bosque):
        if bosque[i] == 1:
            if suceso_aleatorio(f):
                bosque[i] = -1
        i = i + 1
    return bosque 

#bosque = rayos(bosque, 30)

def propagacion(bosque):
    i = 0 
    while i < len(bosque) - 1:
        if bosque[i] == -1 and bosque[i + 1] == 1:
                bosque[i + 1] = -1
        i = i + 1
   
    i = len(bosque) - 1 
    while i > 0:
        if bosque[i] == -1 and bosque[i - 1] == 1:
            bosque[i - 1] = -1
        i = i - 1
    
    return bosque

#bosque = propagacion(bosque)

def limpieza(bosque):
    i = 0
    while i < len(bosque):
        if bosque[i] == -1:
            bosque[i] = 0
        i = i + 1
    return bosque

#bosque = limpieza(bosque)

def dinamica(n, a, p, f):
    i = 0
    cant_arboles_año = np.repeat([0], a)
    while i < a:
        bosque = generar_bosque(n)
        brotes(bosque, p)
        rayos(bosque, f)
        propagacion(bosque)
        limpieza(bosque)
        cant_arboles_año[i] = cuantos(bosque, 1)
        i = i + 1
    return sum(cant_arboles_año)/a
        
#9 item a (el de sobrevivientes)
def arboles_sobrevivientes(f, a, n):
    promedios = []
    p = 0
    while p <= 100:
        promedio = dinamica(n, a, p, f)
        promedios.append(promedio)
        p = p + 1
    return promedios 

#9 item b (el de optimo)
def p_optimo(f, a, n):
    promedios = arboles_sobrevivientes(f, a, n)
    max_sobrevivientes = promedios[0]
    p_opt = 0
    
    i = 1 
    while i < len(promedios):
        if promedios[i] > max_sobrevivientes:
            max_sobrevivientes = promedios[i]
            p_opt = i
        i = i + 1
    return p_opt
        