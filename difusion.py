import numpy as np
import matplotlib.pyplot as plt 
import random

def crear_recipiente(n_filas, m_columnas):
    recipiente = np.zeros((n_filas, m_columnas), np.int16)

    for i in range (recipiente.shape[0]):#recorrer filas
        for j in range(recipiente.shape[1]): #recorrer columnas
            
            if i == 0 or j == 0:
                recipiente[i,j] = -1
                
            if i == recipiente.shape[0] - 1 or j == recipiente.shape[1] - 1:
                recipiente[i,j] = -1
                
    return recipiente

def visualizar_recipiente(recipiente):
    plt.figure()
    cmap = plt.cm.Blues 
    cmap.set_under("black") 
    plt.imshow(recipiente, cmap=cmap, vmin=0) 
    plt.colorbar() 
    plt.show() 
    
def agregar_particulas(recipiente, posicion, cantidad):
    recipiente[posicion] = recipiente[posicion] + cantidad
    
    return recipiente

def es_borde(recipiente, posicion):
    if recipiente[posicion] == -1:
        borde = True
    else:
        borde = False
    return borde

def vecinos(recipiente, posicion):
    lista_vecinos = []
    i,j = posicion
    
    vecino1 = (i+1, j)
    vecino2 = (i-1, j)
    vecino3 = (i, j+1)
    vecino4 = (i, j-1)
    
    if es_borde(recipiente, vecino1) == False:
        lista_vecinos.append(vecino1)
    if es_borde(recipiente, vecino2) == False:
        lista_vecinos.append(vecino2)    
    if es_borde(recipiente, vecino3) == False:
        lista_vecinos.append(vecino3)
    if es_borde(recipiente, vecino4) == False:
        lista_vecinos.append(vecino4)
    
    return lista_vecinos

def dame_uno_al_azar(lista):
    tot_elementos = len(lista)
    azar = random.randint(0, tot_elementos - 1)
    elemento = lista[azar]
    
    return elemento

def mover_particula(recipiente, posicion):
    listavecinos = vecinos(recipiente, posicion)
    if not listavecinos:  # No hay vecinos validos
        return recipiente
    
    casilla_azar = dame_uno_al_azar(listavecinos)
    
    if recipiente[posicion] > 0:
        recipiente[posicion] -= 1
        recipiente[casilla_azar] += 1
    
    return recipiente

def mover_muchas_particulas(recipiente, posicion, cantidad):
    for i in range(cantidad):
        recipiente = mover_particula(recipiente, posicion)

    return recipiente

def mover_particulas_recipiente(recipiente, recipiente_original):
    for i in range(recipiente.shape[0]):
        for j in range(recipiente.shape[1]):
            if recipiente[i, j] > 0:
                cantidad = recipiente[i, j]
                recipiente = mover_muchas_particulas(recipiente, (i, j), cantidad)
    return recipiente

def evolucionar_recipiente(recipiente, k):
    for i in range(k):
        recipiente = mover_particulas_recipiente(recipiente, recipiente)
    return recipiente

def inicializar_particulas(recipiente, cantidad):
    for i in range(1, recipiente.shape[0] - 1):
        recipiente = agregar_particulas(recipiente, (i, 1), cantidad)
    return recipiente

def simular_difusion_horizontal():
    recipiente = crear_recipiente(35, 35)
    recipiente = inicializar_particulas(recipiente, 50)

    for i in range(10):
        visualizar_recipiente(recipiente)
        recipiente_ref = np.copy(recipiente)
        recipiente = mover_particulas_recipiente(recipiente, recipiente_ref)
        for j in range(29):
            recipiente_ref = np.copy(recipiente)
            recipiente = mover_particulas_recipiente(recipiente, recipiente_ref)

    visualizar_recipiente(recipiente)
    return recipiente


