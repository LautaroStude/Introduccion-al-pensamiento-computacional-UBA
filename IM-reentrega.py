import numpy as np
import random
import matplotlib.pyplot as plt


def obtener_imagen(nom_arch):
    im = plt.imread(nom_arch)
    return im


def separar_canales(imagen):
    r1 = imagen[:, :, 0]
    r2 = imagen[:, :, 1]
    r3 = imagen[:, :, 2]
    return r1, r2, r3


def seleccionar_canal(imagen, nombre_canal):
    copia_imagen = np.copy(imagen)
    r, g, b = separar_canales(copia_imagen)
    if nombre_canal == "rojo":
        copia_imagen[:, :, 1] = 0
        copia_imagen[:, :, 2] = 0
  
    elif nombre_canal == "verde":
        copia_imagen[:, :, 0] = 0
        copia_imagen[:, :, 2] = 0
    elif nombre_canal == "azul":
        copia_imagen[:, :, 0] = 0
        copia_imagen[:, :, 1] = 0
    return copia_imagen


def convertir_a_grises(imagen):
    R, G, B = separar_canales(imagen)
    res = 0.299 * R + 0.587 * G + 0.114 * B
    return res 


def multiplicar_y_sumar(array1, array2):
    sum = np.sum(array1 * array2)
    return sum


def aplicar_stencil_a_pos(array, posicion, stencil):
    x, y = posicion
    margen = stencil.shape[0] // 2
    recorte = array[x - margen : x + margen + 1, y - margen : y + margen + 1]
    res = multiplicar_y_sumar(recorte, stencil)
    return res


def aplicar_stencil(array, stencil):
    n, m = array.shape
    salida = np.copy(array)
    margen = stencil.shape[0] // 2
    for i in range(margen, n - margen):
        for j in range(margen, m - margen):
        
            salida[i, j] = aplicar_stencil_a_pos(array, (i, j), stencil)
    return salida


def suavizar(imagen):
    stencil = np.array(
        [[1 / 12, 1 / 8, 1 / 12], [1 / 8, 1 / 6, 1 / 8], [1 / 12, 1 / 8, 1 / 12]]
    )
    res = aplicar_stencil(imagen, stencil)
    return res


def suavizar_k_veces(imagen, k):
    resultado = np.copy(imagen)
    for i in range(k):
        res = suavizar(resultado)
    return res


def combinar_canales(r, g, b):
 
    n, m = r.shape
    resultado = np.zeros((n, m, 3))
    resultado[:, :, 0] = r
    resultado[:, :, 1] = g
    resultado[:, :, 2] = b
    return resultado


def suavizar_color(imagen):
    R, G, B = separar_canales(imagen)
    r_suav = suavizar(R)
    g_suav = suavizar(G)
    b_suav = suavizar(B)
    res = combinar_canales(r_suav, g_suav, b_suav)
    return res


def suavizar_color_k_veces(imagen, k):
    R, G, B = separar_canales(imagen)
    r_suav = suavizar_k_veces(R, k)
    g_suav = suavizar_k_veces(G, k)
    b_suav = suavizar_k_veces(B, k)
    res = combinar_canales(r_suav, g_suav, b_suav)
    return res


def guardar_imagen(imagen, nombre_archivo):
    plt.imsave(nombre_archivo, imagen)
    return