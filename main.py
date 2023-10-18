import random

#se usa random para obtener palabra aleatoria
def obtener_palabra_aleatoria():
    palabras=["perro","gato","mouse","computadora","python","javascript"]
    #mediante la funcion choice vamos a introducir una palabra al azar de la lista anterior
    palabra_aleatoria=random.choice(palabras)
    return palabra_aleatoria
#muestra el estado actual del juego
def mostrar_tablero(palabra_secreta,letras_adivinadas):
    tablero=""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero+=letra
        else:
            tablero+="_"
    print(tablero)
#funcion principal
def jugar_ahorcado():
    palabra_secreta=obtener_palabra_aleatoria()
    letras_adivinadas=[]        
    intentos_restantes=6

    while intentos_restantes>0:
        mostrar_tablero(palabra_secreta, letras_adivinadas)
        letra=input("introduce una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya has introducido esa letra. Prueba con otra letra")
        #se usa continue para saltarnos los demas pasos y volver aqui
            continue  
        if letra in palabra_secreta:
        #mediante append se agrega a la lista letras adivinadas
            letras_adivinadas.append(letra)
         #funcion set para comparar si el conjuntos de letras adivinadas y el conjunto de palabras secretas son iguales 
            if set(letras_adivinadas)==set(palabra_secreta):
                print("Felicidades, has acertado la palabra")
                break
        else:
            intentos_restantes-=1
            print(f"Letra incorrecta. Te quedan {intentos_restantes}")
    if intentos_restantes==0:
        print(f"Has perdido. La palabra secreta era: {palabra_secreta}")

jugar_ahorcado()                        