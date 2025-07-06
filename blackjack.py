import random
import matplotlib.pyplot as plt
import numpy as np

def crear_mazo(n): # "As" es la carta As
    mazo = ["As",2,3,4,5,6,7,8,9,10,10,10,10]*4 * n # n equivale al nunmero de mazos
    random.shuffle(mazo)
    return mazo

def tomar_carta(mazo): 
    carta = mazo.pop()
    return carta 

def verif_en_mano(mano, elemento): # esta funcion verifica en que posicion de la mano se encuentra el elemento indicado
    pos = [] # se agregan a una lista con las posiciones como valores
    for i in range(len(mano)):
        if mano[i] == elemento:
            pos.append(i)
    
    return pos


def calcular_mano(mano):
    pos = verif_en_mano(mano, "As") # esta primera parte cambia los "As" por 11
    a = 11
    for i in range(len(pos)):
        temp = pos[i]
        mano.pop(temp)    
        mano.append(a)
    
    pos = verif_en_mano(mano, 11) # esta segunda parte calcula para ver si conviene que el "As" valga 11 o 1
    if sum(mano) > 21:
        for i in range(len(pos)):
            temp = pos[i]
            mano.pop(temp)
            mano.append(1)
            
    total = sum(mano)

    return total

def jugar_mano(mazo, tope): # juega la mano hasta el tope indicado
    mano = []
    puntaje = 0
    while puntaje < tope:
        carta = tomar_carta(mazo)
        mano.append(carta)
        total = calcular_mano(mano)
        puntaje = total
        print(mano)
        
    return total

def jugar_partida(tope, n):
    #Simulacion de partida con tope y n barajas repartidas
    mazo = crear_mazo(n)
    mano_crupier = []
    mano_jug = []
    #Primera mano para cada uno
    carta_jug = tomar_carta(mazo)
    mano_jug.append(carta_jug)
    carta_crup = tomar_carta(mazo)
    mano_crupier.append(carta_crup)
    
    #Dar carta hasta que no pueda mas dependiendo el tope
    puntaje_jug = calcular_mano(mano_jug)
    while puntaje_jug < tope and puntaje_jug <= 21:
        carta = tomar_carta(mazo)
        mano_jug.append(carta)
        puntaje_jug = calcular_mano(mano_jug)
    #Ya jugado el jugador va el crupier, con min de 17 siempre fijo    
    puntaje_crup = calcular_mano(mano_crupier)
    while puntaje_crup < 17 and puntaje_crup <= 21:
        carta = tomar_carta(mazo)
        mano_crupier.append(carta)
        puntaje_crup = calcular_mano(mano_crupier)
    return puntaje_jug, puntaje_crup

def quien_gano(tope, n): # dependiendo del resultado la funcion va a decidir si gana el crupier (-1), el jugador (1), o es empate (0)
    res = jugar_partida(tope, n)
    i, j = res
    gano = 0
    if j > i and j <= 21 or i > 21:
        gano = -1 # -1 representa la victoria del crupier
    elif j == i and i < 21:
        gano = 0 # 0 representa un empate
    elif i > j and i <= 21:
        gano = 1 # 1 representa la victoria del jugador
    return gano

def partida_con_apuesta(tope, dinero_total, dinero_apostado): # simula una partida apostando el dinero indicado
    partida = quien_gano(tope, 1) # como la consigna pide un mazo, hago que la partida se juege con un solo mazo
    if dinero_apostado <= dinero_total: # si no hay plata suficiente para apostar devuelve el total ingresado
        if partida == -1:
            dinero_total = dinero_total - dinero_apostado
        elif partida == 1:
            dinero_total = dinero_total + dinero_apostado * 2

    return dinero_total

def jugar_con_apuestas(tope, dinero_total, dinero_apostado):
    dinero = [] # registro el dinero a lo largo del tiempo en esta lista
    while dinero_total >= dinero_apostado:
        partida = partida_con_apuesta(tope, dinero_total, dinero_apostado)
        dinero_total = partida
        dinero.append(dinero_total)

    return dinero

# Pregunta 1

def simular_topes(n): # simula una partida por cada tope del 1 al 21 (n refiere al numero de mazos)
    tope = 1
    lista_res = []
    for tope in range(21):
        res = quien_gano(tope, n)
        lista_res.append(res)
        
    return lista_res

def simular_topes_multiple(repeticiones, n): # Simula una partida con topes del 1 al 21
    simulaciones = np.zeros((repeticiones, 21))
    for rep in range(repeticiones):
        partida = simular_topes(n)
        simulaciones[rep, ] = partida
        
    return simulaciones

def probabilidad_topes(simulaciones): # Simula una partida una cierta cantidad de veces y calcula la probabilidad de ganar con cierto tope
    repeticiones = simulaciones.shape[0]
    prop = []
    for j in range(21):
        total = 0
        for i in range(repeticiones):
            if simulaciones[i, j] == 1:
                total = total + 1
            else:
                total = total
           
            chance = (total/repeticiones) * 100
        
        prop.append(chance)
        
    return prop

def graficar_prob_topes(topes, prob): # Grafica la probabilidad de ganar con topes del 1 al 21 (requiere como parametro estos resultados de las funciones anteriores)
    plt.title("Chances de victoria en Blackjack")
    plt.xlabel("Topes", fontsize = 16)
    plt.ylabel("Chances")
    plt.bar(topes, prob)
    plt.ylim(0,100)
    plt.show()
    
    return

"""
sim = simular_topes_multiple(100, 2)
prob = probabilidad(sim)
topes = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]

graficar_prob(topes, prob)     
"""

# Pregunta 2

def simular_mazos(tope, tope_mazos):    
    mazos = 1
    victorias = []
    while mazos <= tope_mazos:
        partida = quien_gano(tope, mazos)
        if partida == 1:
            victorias.append(partida)
        else:
            victorias.append(0)
            
        mazos = mazos + 1

    return victorias

def simular_mazos_multiple(repeticiones, tope, mazos):
    simulaciones = np.zeros((repeticiones, mazos))
    for rep in range(repeticiones):
        partida = simular_mazos(tope, mazos)
        simulaciones[rep, ] = partida
    
    return simulaciones

def probabilidad_mazos(simulaciones): # Simula una partida una cierta cantidad de veces y calcula la probabilidad de ganar con cierto tope
    repeticiones = simulaciones.shape[0]
    prop = []
    for j in range(simulaciones.shape[1]):
        total = 0
        for i in range(repeticiones):
            if simulaciones[i, j] == 1:
                total = total + 1
            else:
                total = total
           
            chance = (total/repeticiones) * 100
        
        prop.append(chance)
        
    return prop

def graficar_prob_mazos(mazos, prob): # Grafica la probabilidad de ganar con topes del 1 al 21 (requiere como parametro estos resultados de las funciones anteriores)
    plt.title("Chances de victoria en Blackjack")
    plt.xlabel("Mazos", fontsize = 16)
    plt.ylabel("Chances")
    plt.bar(mazos, prob)
    plt.ylim(0,100)
    plt.show()
    
    return

"""
partidas = simular_mazos_multiple(100, 17, 20)
prob = probabilidad_mazos(partidas)
mazos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
graficar_prob_mazos(mazos, prob)
"""

def jugador_serial(dinero_inicial, apuesta_maxima, max_partidas):

    dinero = dinero_inicial
    evo_dinero = [dinero]
    #lista en donde se guarda cada dinero que tenia disponible
    partidas_jugadas = 0
    
    while dinero >= apuesta_maxima and partidas_jugadas < max_partidas:
        resultado = quien_gano(21, 1)
        
        if resultado == 1:  
            dinero += apuesta_maxima
        elif resultado == -1: 
            dinero -= apuesta_maxima
        
        evo_dinero.append(dinero)
        partidas_jugadas += 1
    
    return evo_dinero

def jugador_moderado(dinero_inicial, apuesta_promedio, max_partidas):

    dinero = dinero_inicial
    evo_dinero = [dinero]
    partidas_jugadas = 0
    
    while dinero >= apuesta_promedio and partidas_jugadas < max_partidas:
        resultado = quien_gano(18, 1)
        
        if resultado == 1:  
            dinero += apuesta_promedio
        elif resultado == -1: 
            dinero -= apuesta_promedio
        
        evo_dinero.append(dinero)
        partidas_jugadas += 1
    
    return evo_dinero

def jugador_reservado(dinero_inicial, apuesta_minima, max_partidas):

    dinero = dinero_inicial
    evo_dinero = [dinero]
    partidas_jugadas = 0
    
    while dinero >= apuesta_minima and partidas_jugadas < max_partidas:
        resultado = quien_gano(16, 1)
        
        if resultado == 1: 
            dinero += apuesta_minima
        elif resultado == -1: 
            dinero -= apuesta_minima
        
        evo_dinero.append(dinero)
        partidas_jugadas += 1
    
    return evo_dinero

def simular_perfiles(simulaciones):
    
    #simula múltiples partidas para cada perfil de jugador  
    resultados_serial = []
    resultados_moderado = []
    resultados_reservado = []
    
    for i in range(simulaciones):
        serial = jugador_serial(200, 15, 100)
        moderado = jugador_moderado(200, 10, 100)
        reservado = jugador_reservado(200, 5, 100)
        
        resultados_serial.append(serial)
        resultados_moderado.append(moderado)
        resultados_reservado.append(reservado)
    
    return resultados_serial, resultados_moderado, resultados_reservado

def graficar_perfiles(resultados_serial, resultados_moderado, resultados_reservado, num_partidas):
    #hace un promedio y grafica para cada perfil, para que no tome solo una partida
    prom_serial = []
    prom_moderado = []
    prom_reservado = []
    
    for partida in range(num_partidas):
        #promedio del serial
        sum_serial = 0
        contador_serial = 0
        for simulacion in resultados_serial:
            if partida < len(simulacion):
                sum_serial = sum_serial + simulacion[partida]
                contador_serial = contador_serial + 1
        if contador_serial > 0:
            prom_serial.append(sum_serial / contador_serial)
        else:
            prom_serial.append(0)
        
        #promedio del moderado
        sum_moderado = 0
        contador_moderado = 0
        for simulacion in resultados_moderado:
            if partida < len(simulacion):
                sum_moderado = sum_moderado + simulacion[partida]
                contador_moderado += 1
        if contador_moderado > 0:
            prom_moderado.append(sum_moderado / contador_moderado)
        else:
            prom_moderado.append(0)
        
        #promedio del reservado
        sum_reservado = 0
        contador_reservado = 0
        for simulacion in resultados_reservado:
            if partida < len(simulacion):
                sum_reservado = sum_reservado + simulacion[partida]
                contador_reservado += 1
        if contador_reservado > 0:
            prom_reservado.append(sum_reservado / contador_reservado)
        else:
            prom_reservado.append(0)
    
    plt.figure()
    plt.plot(prom_serial, label='Serial')
    plt.plot(prom_moderado, label='Moderado')
    plt.plot(prom_reservado, label='Reservado') 
    plt.xlabel('Partidas')
    plt.ylabel('Dinero')
    plt.legend()
    plt.show()
    #para probarlo en la consola, hago por ej: serial, moderado, reservado = simular_perfiles(100)
    #luego hago graficar_perfiles(serial, moderado, 100)                
    return