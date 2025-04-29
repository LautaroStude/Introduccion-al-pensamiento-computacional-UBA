import random 

def cuantas_figus(figus_total):
    #dado cant_figus devuelve contador 
    album = [0] * figus_total
    contador = 0 

    while sum(album) < len(album):
        figu = random.randint(0, len(album) - 1)
        contador = contador + 1 
        album[figu] = 1
    
    return contador

def cuantas_figus_multiple(figus_total, n_albumes):
    # se ingresan x cantidad de figuritas necesitadas por album + cant albumes y devuelve una lista
    lista_albumes =[]
    i = 0
    while n_albumes > i:
        intentos = cuantas_figus(figus_total)
        lista_albumes.append(intentos)
        i = i + 1
    return lista_albumes

def promedio_figus(figus_total, n_albumes):
    promedio = cuantas_figus_multiple(figus_total, n_albumes)

    return sum(promedio)/len(promedio)

def chance_llenar_album(cant_compradas_reales, cant_figus_max):
    #cociente para determinar la chance de llenar album con x cantidad maxima de figuritas
    contadorFigusMax=0

    for x in range(len(cant_compradas_reales)):
        if cant_compradas_reales[x] <= cant_figus_max:
            contadorFigusMax+=1

    chanceLlenarAlbum=(contadorFigusMax/len(cant_compradas_reales))

    return chance_llenar_al

def chance_llenar_album_multiple(figus_Total, cant_figus_max, n_albumes):
    #chance de completar x cantidad de albumes con un tamaño x y imponiendole una cant max de figus para comprar
    cant_compradas_reales=cuantas_figus_multiple(figus_Total,n_albumes)
    contadorFigusMax=0

    for x in range(len(cant_compradas_reales)):
        if cant_compradas_reales[x] <= cant_figus_max:
            contadorFigusMax+=1

    chanceLlenarAlbum=(contadorFigusMax/len(cant_compradas_reales))

    return chance_llenar_album_multi
