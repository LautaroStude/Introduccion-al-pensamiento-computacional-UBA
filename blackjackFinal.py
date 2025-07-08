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
    #primera parte encuentra la posicion de los ases y los cambia por 11
    pos = verif_en_mano(mano, "As") 
    a = 11
    for i in range(len(pos)):
        temp = pos[i] - i  
        mano.pop(temp)    
        mano.append(a)
    #encuentra donde esta esos 11 y si la suma es mayor a 21 los cambia por 1
    pos = verif_en_mano(mano, 11) 
    if sum(mano) > 21:
        for i in range(len(pos)):
            temp = pos[i] - i  
            mano.pop(temp)
            mano.append(1)
            
    total = sum(mano)
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
    elif i > j and i <= 21 or j > 21:
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

# Pregunta 1 clase 2

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
prob = probabilidad_topes(sim)
topes = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]

graficar_prob_topes(topes, prob)     
"""

# Pregunta 2 clase 2

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

#pregunta 3 clase 2
def jugador_serial(dinero_inicial, apuesta_maxima, max_partidas):

    dinero = dinero_inicial
    evo_dinero = [dinero]
    #lista en donde se guarda cada dinero que tenia disponible
    partidas_jugadas = 0
    
    while dinero >= apuesta_maxima and partidas_jugadas < max_partidas:
        resultado = quien_gano(21, 2)
        
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
        resultado = quien_gano(18, 2)
        
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
        resultado = quien_gano(16, 2)
        
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
    #luego hago graficar_perfiles(serial, moderado, reservado, 100)                
    return

def jugar_partida_mod(tope, tope_crupier, n): # Funciona de la misma manera que "jugar_partida", con la diferencia de que puedo modificar el tope del crupier
    mazo = crear_mazo(n)
    mano_crupier = []
    mano_jug = []
   
    carta_jug = tomar_carta(mazo)
    mano_jug.append(carta_jug)
    carta_crup = tomar_carta(mazo)
    mano_crupier.append(carta_crup)   
   
    puntaje_jug = calcular_mano(mano_jug)
    while puntaje_jug < tope and puntaje_jug <= 21:
        carta = tomar_carta(mazo)
        mano_jug.append(carta)
        puntaje_jug = calcular_mano(mano_jug)
    # El tope del crupier deja de ser siempre 17 y pasa a ser modificable
    puntaje_crup = calcular_mano(mano_crupier)
    while puntaje_crup < tope_crupier and puntaje_crup <= 21:
        carta = tomar_carta(mazo)
        mano_crupier.append(carta)
        puntaje_crup = calcular_mano(mano_crupier)
    return puntaje_jug, puntaje_crup

def quien_gano_mod(partida): # Similar a "quien gano", pero recibe como parámetro el resultado de la función
    res = partida
    i, j = res
    gano = 0
    if j > i and j <= 21 or i > 21:
        gano = -1 # -1 representa la victoria del crupier
    elif j == i and i < 21:
        gano = 0 # 0 representa un empate
    elif i > j and i <= 21 or j > 21:
        gano = 1 # 1 representa la victoria del jugador
    return gano

def simulacion_mod(n): # devuelve un array ordenado por filas (topes del jugador del 15 al 21) y columnas (topes del crupier de 15 a 21)
    topes_jugador = []
    min_jugador = 15
    while min_jugador <= 21:
        min_crupier = 15 # el tope minimo del crupier va a ser 15
        topes_crupier = []
        while min_crupier <= 21:
            partida = jugar_partida_mod(min_jugador, min_crupier, n)
            ganador = quien_gano_mod(partida)
            topes_crupier.append(ganador)
            min_crupier += 1
        
        topes_jugador.append(topes_crupier)
        min_jugador += 1
    array_topes = np.array(topes_jugador)
    return array_topes



def simulacion_mod_multiple(repeticiones, n): # Simula varias partidas con el sistema de "simulacion_mod" pero como arrays de 7x7xN
    simulaciones = np.zeros((repeticiones, 7, 7)) # siempre van a ser de 7x7x(rep), ya que las simulaciones abarcan 7x7 posibilidades de topes distintas (por los topes del crupier y del jugador)
    for rep in range(repeticiones):
        partida = simulacion_mod(n)
        simulaciones[rep, :, :] = partida
        
    return simulaciones # devuelve un array de dimension 3 con las partidas repetidas

def probabilidad_simulacion_mod(simulaciones): # Devuelve un array con las probabilidades de victoria por cada posicion del array, ordenado por filas (topes del jugador) y columnas (topes del crupier) de 15 a 21
    repeticiones = simulaciones.shape[0]
    total_jugador = np.zeros((7,7))
    total_crupier = np.zeros((7,7))
        
    for j in range(7):
        for k in range(7):
            total = 0
            for l in range(repeticiones):
                if simulaciones[l,j,k] == 1:
                    total += 1
                else:
                    total = total
                
                chance = (total/repeticiones) * 100
                
            total_crupier[j, k] = chance
        
    total_jugador[:, :] = total_crupier

    return total_jugador

sim = simulacion_mod_multiple(100, 2)
sim2 = probabilidad_simulacion_mod(sim)

def grafico_probabilidad_simulacion_mod(simulacion):     
    print(simulacion)
    plt.figure()
    plt.plot(simulacion[0, :], label='15')
    plt.plot(simulacion[1, :], label='16')
    plt.plot(simulacion[2, :], label='17')
    plt.plot(simulacion[3, :], label='18')
    plt.plot(simulacion[4, :], label='19')
    plt.plot(simulacion[5, :], label='20')
    plt.plot(simulacion[6, :], label='21') 
    plt.xlabel('Topes del crupier')
    plt.ylabel('Chances de victoria')
    plt.xticks(ticks=[0, 1, 2, 3, 4, 5, 6], labels=[15, 16, 17, 18, 19, 20, 21])
    plt.legend(title="Topes del jugador")
    plt.show()

    return

def simular_comb_cartas(num_cartas, repeticiones, n):
    #dependiendo un numero de cartas como parametro y x repepeticiones devuelve una lista con las distintas sumas
    #tambien usa el parametro n que es para la cantidad de mazos en la partida
    puntajes = []
    #doble for para recorrer la cant de repeticiones y el segundo para tomar cartas hasta la cant indicada
    for i in range(repeticiones):
        mazo = crear_mazo(n)
        mano = []
        
        for j in range(num_cartas):
            carta = tomar_carta(mazo)
            mano.append(carta)
        un_puntaje = calcular_mano(mano) 
        puntajes.append(un_puntaje)
    return puntajes

def graficar_comb_cartas(n, repeticiones):
    #n se refiere a la cantidad de mazos utilizados
    #devuelve una lista por variable con x cantidad de repeticiones 
    puntaje_2_cartas = simular_comb_cartas(2, repeticiones, n)
    puntaje_3_cartas = simular_comb_cartas(3, repeticiones, n)
    puntaje_4_cartas = simular_comb_cartas(4, repeticiones, n)
    
    #hace el promedio dentro de esa lista para luego plasmarlo en el grafico
    prom_2 = sum(puntaje_2_cartas) / len(puntaje_2_cartas)
    prom_3 = sum(puntaje_3_cartas) / len(puntaje_3_cartas)
    prom_4 = sum(puntaje_4_cartas) / len(puntaje_4_cartas)
    
    cant_cartas = [2,3,4]
    promedios = [prom_2, prom_3, prom_4]
    
    plt.bar(cant_cartas, promedios)
    plt.xlabel('Numero de cartas por mano')
    plt.ylabel('Suma promedio')
    plt.title('Puntaje promedio por cantidad de cartas')
    plt.show()
    
    return

def chance_no_pasarse(repeticiones, n):
    #n cantidad de mazos
    #repeticiones son las veces que simula la funcion previa, mientras sea mas grandes mas fiable
    lista_4_cartas = simular_comb_cartas(4, repeticiones, n)
    total = 0
    contador = 0
    #recorrer la lista lista_4_cartas y creo contador y total para contar las veces que el re
    for i in range(len(lista_4_cartas)):
        if lista_4_cartas[i] <= 21:
            total += 1
            contador += 1
        else:
            contador += 1
    chances = (total/contador) * 100
    return chances
            
def siguiente_carta(mazo): # revisa la siguiente carta del mazo dado
    carta = tomar_carta(mazo)
    if carta == "As":
        carta = 1 # para la siguiente funcion, es conveniente que el "As" siempre valga uno
    return carta

def chance_no_pasarse_lista(n): # Devuelve una lista, donde la posicion de la lista indica la cantidad de cartas y el valor (0 o 1) indica si la siguiente carta hace que el jugador se pase de 21
    mano = []
    lista_chances = []
    total = 0
    while total < 21:
        mazo = crear_mazo(n)
        carta = tomar_carta(mazo)
        mano.append(carta)
        total = calcular_mano(mano)
        if calcular_mano([total + siguiente_carta(mazo)]) > 21:
            chances = 1
            lista_chances.append(chances)
            total = total + siguiente_carta(mazo)
            while len(lista_chances) < 8: # Se le da un valor máximo de 8 cartas, rellenando con 1 (pasarse) hasta len(lista_chances) 8
                lista_chances.append(1)
        else: 
            chances = 0
            lista_chances.append(chances)
        
    while len(lista_chances) > 8: # Se elimina cualquier 1 que haya quedado demás para que la funcion devuelva una lista con 8 elementos
        lista_chances.pop()

    return lista_chances

def array_chance_pasarse(n, repeticiones):  # repite la funcion de arriba y ordena los resultados en un array
    simulaciones = np.ones((repeticiones, 8)) # Debido a que la lista tiene 8 elementos, el array va a tener longitud de 8 columnas
    for rep in range(repeticiones):
        partida = chance_no_pasarse_lista(n)
        simulaciones[rep, ] = partida
    
    return simulaciones

def porcentaje_chance_pasarse(simulaciones): # Dado el array de arriba con las repeticiones, se calcula el porcentaje de que la suma del puntaje de la mano y la siguiente carta del mazo sea mayor a 21
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

def graficar_chance_pasarse(cartas, prob): # Hace un gráfico del porcentaje
    plt.title("Chances de pasarse de 21 según el número de cartas en la mano")
    plt.xlabel("Cantidad de cartas", fontsize = 16)
    plt.ylabel("Chances")
    plt.bar(cartas, prob)
    plt.ylim(0,100)
    plt.show()
    
    return
"""
arr = array_chance_pasarse(2, 10000)
arr2 = porcentaje_chance_pasarse(arr)
graficar_chance_pasarse([1,2,3,4,5,6,7,8], arr2)
"""