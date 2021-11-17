letras= "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

cadena= "Hola,mundo"

for letra in cadena:
    posicion = 0
    while posicion < len(letras):
        l = letras[posicion]
        if l == letra:
            break   
        posicion +=1

    if posicion ==len(letras):
        print("no encontrado")
    else:
        #Obtener símbolo morse de posicion = posicion
        print("{} -{}".format(letra, posicion))