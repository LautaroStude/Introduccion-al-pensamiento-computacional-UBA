import random


def tirar_cubilete():
    dados = [] #espacios vacios
    i = 0 #cantidad de veces tiradas
    while i < 5: #mientras no sean 5 los dados creados
        dados.append(random.randint(1, 6))  
        i = i + 1
    return dados

def cuantos_hay(elemento, lista):
    i = 0
    contador = 0
    while i < len(lista):
        if elemento == lista[i]:
            contador = contador +1   
        i = i +1
    return contador

def puntos_por_unos(lista):
    unos = cuantos_hay(1, lista)
    puntos = unos * 100
    if unos == 3:
        puntos = puntos + 1000
    elif unos == 4:
        puntos = puntos + 1100
    elif unos == 5:
        puntos = puntos + 10000
    return puntos 

def puntos_por_cincos(lista):
    cincos = cuantos_hay(5, lista)
    puntos = cincos * 50
    if cincos == 3:
        puntos = puntos + 500
    elif cincos == 4:
        puntos = puntos + 550
    elif cincos == 5:
        puntos = puntos + 600
    return puntos 

def total_puntos(lista):
    puntos = puntos_por_unos(lista) + puntos_por_cincos(lista)
    return puntos

def jugar_ronda(cant_jugadores):
    puntos = [0] * cant_jugadores
    i = 0
    while i < cant_jugadores:
      dados = tirar_cubilete()
      total = total_puntos(dados)
      puntos[i] = total  
      i +=1
    return puntos

def acumular_puntos(puntajes_acumulados, puntajes_ronda_actual):
    i = 0  
    while i < len(puntajes_acumulados):
        puntajes_acumulados[i] = puntajes_acumulados[i]+puntajes_ronda_actual[i]
        i = i + 1
    return puntajes_acumulados

def hay_10mil(puntajes_acumulados):
    i=0
    for i in range(len(puntajes_acumulados)):
        if puntajes_acumulados[i]>=10000:
            return True
        else:
            return False

def partida_completa(cant_jugadores):
    contadorRonda = 0
    puntajesJugadoresAcumulado =[0]*cant_jugadores
    i = True
    while i != hay_10mil(puntajesJugadoresAcumulado):
        puntajesJugadoresRonda=jugar_ronda(cant_jugadores)
        puntajesJugadoresAcumulado=acumular_puntos(puntajesJugadoresAcumulado,puntajesJugadoresRonda)
        contadorRonda+=1

    return contadorRonda

def cant_rondas_promedio(cant_jugadores, cant_partidas):
    suma=0
    for x in range(cant_partidas):
        suma+=partida_completa(cant_jugadores)
    promedio=suma/cant_partidas

    return promedio

def chance_de_terminar(cant_jugadores, max_rondas, cant_partidas):
    contadorPartidas = 0
    for x in range(cant_partidas):
        if partida_completa(cant_jugadores) <= max_rondas:
            contadorPartidas+=1

    chanceTerminar = (contadorPartidas/cant_partidas) * 100 
    return chanceTerminar

print(chance_de_terminar(20,18,1000))