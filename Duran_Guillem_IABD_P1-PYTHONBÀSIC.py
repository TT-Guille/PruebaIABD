#IMPORT RANDOM
import random

#FUNCIONES
def puntuacion():
    print(f"Victorias:  {victoriasUsuario} - Victorias Maquina: {victoriasMaquina}")

#MENU
menu = """
Bienvenidos, escoged una opcion

[1] Adivina Numero 
[2] Piedra Papel Tijeras
[3] Ahorcado 

"""
print(menu)

opcion = input('Escoge una opcion entre 1 y 3: ')

#OPCION 1
if opcion == '1':
    #VARIABLES
    bucle = True
    vida = 3
    arrayNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numeroAleatorio = int(random.choice(arrayNumeros))

    #ADIVINAR NUMERO
    while bucle and vida > 0:
        numeroAdivinado = int(input('Escoge un numero entre el 1 y el 10'))
        if numeroAleatorio == numeroAdivinado:
            print(f"Lo has conseguido, el numero es {numeroAdivinado}")
            bucle = False
        #NUMERO MAYOR
        if numeroAleatorio > numeroAdivinado:
            print("El numero es mayor")
            vida = vida - 1
        #NUMERO MENOR
        if numeroAleatorio < numeroAdivinado:
            print("El numero es menor")
            vida = vida - 1
    #SIN VIDAS        
    if vida == 0:
        print("Has perdido, te has quedado sin vidas")

#OPCION 2
elif opcion == '2':
    #VARIABLES
    bucle = True
    victoriasMaquina = 0
    victoriasUsuario = 0
    arrayJuego = ["Piedra", "Papel", "Tijera"]

    #PIEDRA, PAPEL, TIJERA
    while bucle:
        arrayJuegoSelecion = random.choice(arrayJuego)
        opcionUsuario = input('Escoge Piedra, Papel, Tijera: ')
        if opcionUsuario == "Piedra" and arrayJuegoSelecion == "Papel":
            print(f"Has perdido, he sacado {arrayJuegoSelecion}")
            victoriasMaquina = victoriasMaquina + 1
            puntuacion()
        if opcionUsuario == "Piedra" and arrayJuegoSelecion == "Tijera":
            print(f"Has ganado, he sacado {arrayJuegoSelecion}")
            victoriasUsuario = victoriasUsuario + 1
            puntuacion()
        if opcionUsuario == "Piedra" and arrayJuegoSelecion == "Piedra":
            print("Habeis empatado")
            puntuacion()
        if opcionUsuario == "Papel" and arrayJuegoSelecion == "Piedra":
            print(f"Has ganado, he sacado {arrayJuegoSelecion}")
            victoriasUsuario = victoriasUsuario + 1
            puntuacion()
        if opcionUsuario == "Papel" and arrayJuegoSelecion == "Papel":
            print("Habeis empatado")
            puntuacion()
        if opcionUsuario == "Papel" and arrayJuegoSelecion == "Tijera":
            print(f"Has perdido, he sacado {arrayJuegoSelecion}")
            victoriasMaquina = victoriasMaquina + 1
            puntuacion()
        if opcionUsuario == "Tijera" and arrayJuegoSelecion == "Tijera":
            print("Habeis empatado")
            puntuacion()
        if opcionUsuario == "Tijera" and arrayJuegoSelecion == "Papel":
            print(f"Has ganado, he sacado {arrayJuegoSelecion}")
            victoriasUsuario = victoriasUsuario + 1
            puntuacion()
        if opcionUsuario == "Tijera" and arrayJuegoSelecion == "Piedra":
            print(f"Has perdido, he sacado {arrayJuegoSelecion}")
            victoriasMaquina = victoriasMaquina + 1
            puntuacion()
        if victoriasMaquina == 3:
            print("La Maquina ha ganado")
            bucle = False
        if victoriasUsuario == 3:
            print("Has ganado!")
            bucle = False

#OPCION 3
elif opcion == '3':
    #ABRIMOS FICHERO EXTERNO
    with open("30_Palabras.txt", "r") as file:
        allText = file.read()
    words = list(map(str, allText.split()))
    randomWord = random.choice(words)
    # VARIABLES
    listaPalabraAdiv = []
    listaPalabraMost = []
    intentos = len(randomWord) * 2
    letra = ''
    run = True

    #SEPARAMOS PALABRA POR LETRAS
    listaPalabraAdiv = list(randomWord)

    for item in listaPalabraAdiv:
        listaPalabraMost.append('_')

    while run:
        #MOSTRAMOS PALABRA A ADIVINAR
        print(' '.join(listaPalabraMost))

        #PEDIMOS LETRA
        letra = input('Dame una letra: ')
        letra = letra.upper()
        
        #LIMPIAMOS PANTALLA
        for num in range(100):
            print()

        #COMPROBAMOS SI HA FALLADO
        fallo = False

        if letra not in listaPalabraAdiv:
            fallo = True
            intentos = intentos - 1
            print('Has fallado!!!! Te quedan {intentos} intentos'.format(intentos=intentos))
        else:
            #EN CASO DE ADIVINARLO
            for key, value in enumerate(listaPalabraAdiv):
                if value == letra:
                    listaPalabraMost[key] = value

        #COMPROBAMOS SI HA PERDIDO LA PARTIDA
        if intentos <= 0:
            run = False
            print('Has perdido, la palabra '
                'era "{palabra}"'.format(palabra=''.join(listaPalabraAdiv)))
        elif listaPalabraAdiv == listaPalabraMost:
            run = False
            print('Has ganado, la palabra '
                'era "{palabra}"'.format(palabra=''.join(listaPalabraAdiv)))

#SI NO SE ESCOGE UN NUMERO CORRECTO
else:
    print("No has escogido una opcion correcta")
