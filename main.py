import random
import os

def normalize(s):
    # Reemplaza caracteres especiales con su versión sin acento
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def run():
    # Leer el archivo de palabras y elegir una palabra al azar
    with open("./data.txt", "r", encoding="UTF-8") as f:
        lista_pal = list(f)
    palabras = random.choice(lista_pal)
    palabras = normalize(palabras)
    palabra = list(palabras.upper())
    palabra.pop(-1)

    # Inicializar variables para jugar
    caracteres = len(palabra)
    aciertos = 0
    caracteres_puestos = []
    vida = 10
    rayas = []

    # Crear una lista con rayas para mostrar la palabra a adivinar
    for i in range(len(palabra)):
        rayas.append("_")
    print(rayas)

    # Limpiar la pantalla
    os.system("clear")

    # Mostrar el título del juego
    print("""
███████╗██╗░░░░░  ░░░░░██╗██╗░░░██╗███████╗░██████╗░░█████╗░  ██████╗░███████╗██╗░░░░░
██╔════╝██║░░░░░  ░░░░░██║██║░░░██║██╔════╝██╔════╝░██╔══██╗  ██╔══██╗██╔════╝██║░░░░░
█████╗░░██║░░░░░  ░░░░░██║██║░░░██║█████╗░░██║░░██╗░██║░░██║  ██║░░██║█████╗░░██║░░░░░
██╔══╝░░██║░░░░░  ██╗░░██║██║░░░██║██╔══╝░░██║░░╚██╗██║░░██║  ██║░░██║██╔══╝░░██║░░░░░
███████╗███████╗  ╚█████╔╝╚██████╔╝███████╗╚██████╔╝╚█████╔╝  ██████╔╝███████╗███████╗
╚══════╝╚══════╝  ░╚════╝░░╚═════╝░╚══════╝░╚═════╝░░╚════╝░  ╚═════╝░╚══════╝╚══════╝

░█████╗░██╗░░██╗░█████╗░██████╗░░█████╗░░█████╗░██████╗░░█████╗░
██╔══██╗██║░░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
███████║███████║██║░░██║██████╔╝██║░░╚═╝███████║██║░░██║██║░░██║
██╔══██║██╔══██║██║░░██║██╔══██╗██║░░██╗██╔══██║██║░░██║██║░░██║
██║░░██║██║░░██║╚█████╔╝██║░░██║╚█████╔╝██║░░██║██████╔╝╚█████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░
    """)

    # Mostrar el logo del juego
    print("""
KdoddddddddddddddddddddddddddddddddddddddddddddodK
o:0KxddddddddddddddddddddddddddddddddddddddddxK0:o
lcKo:oodkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkd:oKll
llKllOlOMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNllKll
llKllKk0XKKKKKKKKKKKKKKKKKKKKKKKKKKXWMMMMMMMNllKll
llKllOodxdl;cd:,cddddddddddd;;dddddkXMMMMMMMNllKll
lcKllk:xMM0:ldcxXMMMMMMMMMWO;;ONMMMMMMMMMMMMNllKll
llKllk:xMM0,'dKWMMMMMMMM0dolddll0WMMMMMMMMMMNllKll
llKll0d0MM0:dWMMMMMMMMMNl.cXMMNclNMMMMMMMMMMNllKll
llKllNWWMM0:xMMMMMMMMMMWkccdOOdcxWMMMMMMMMMMNllKll
llKllNMMMM0:xMMMMMMMMMMMWWKx;;xKWMMMMMMMMMMMNllKll
llKllNMMMM0:xMMMMMMMMMMMNX0d''d0NMMMMMMMMMMMNllKll
llKllNMMMM0:xMMMMMMMMMNkoodd,,ddokNMMMMMMMMMNllKll
llKllNMMMM0:xMMMMMMMMMWXNWWNllNMNXWMMMMMMMMMNllKll
llKllNMMMM0:xMMMMMMMMMMMMMMNllNMMMMMMMMMMMMMNllKll
llKllNMMMM0:xMMMMMMMMMMMMMWk;;kWMMMMMMMMMMMMNllKll
llKllNMMMM0:xMMMMMMMMMMWOdllkkllOWMMMMMMMMMMNllKll
llKllNMMMM0:xMMMMMMMMMNxloONMMNOlxNMMMMMMMMMNllKll
llKllNMMMM0:xMMMMMMMMMWXWMMMMMMMWXWMMMMMMMMMNllKll
llKllNW0xxl':xxxxxxxxxxxxxxxxxxxxxxxxxxxxx0WNllKll
llKllNWKkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkKWNllKll
llKlcXWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWXclKll
lcXOoddddddddddddddddddddddddddddddddddddddddoOXcl
kcoxxddddddddddddddddddddddddddddddddddddddddxxock
WOollllllllllllllllllllllllllllllllllllllllllllo0W
    """)

    # Repetir mientras que no se hayan adivinado todos los caracteres
    while caracteres != aciertos:
        # Mostrar la palabra con rayas y las vidas que quedan
        print(" ".join(rayas))
        print("Tienes", vida, "vidas")

        # Pedir una letra al usuario
        try:
            letra = input("Ingrese un cáracter porfavor: ").upper()
            if len(letra) > 1 or letra.isnumeric():
                raise TypeError("Solo se puede ingresar una única letra")
        
        # Si el usuario ingresa algo que no es una letra, mostrar un mensaje de error
        except ValueError as ve:
            print(ve)
            continue

        # Si el usuario se queda sin vidas, mostrar un mensaje de que ha perdido y salir del juego
        if vida == 0:
            os.system("clear")
            print("""

▄▄▌            .▄▄ · ▪  ▄▄▄ . ▐ ▄ ▄▄▄▄▄           ▄▄▄·▄▄▄ .▄▄▄  ·▄▄▄▄  ▪  .▄▄ · ▄▄▄▄▄▄▄▄ ..▄▄ · 
██•  ▪         ▐█ ▀. ██ ▀▄.▀·•█▌▐█•██  ▪         ▐█ ▄█▀▄.▀·▀▄ █·██▪ ██ ██ ▐█ ▀. •██  ▀▄.▀·▐█ ▀. 
██▪   ▄█▀▄     ▄▀▀▀█▄▐█·▐▀▀▪▄▐█▐▐▌ ▐█.▪ ▄█▀▄      ██▀·▐▀▀▪▄▐▀▀▄ ▐█· ▐█▌▐█·▄▀▀▀█▄ ▐█.▪▐▀▀▪▄▄▀▀▀█▄
▐█▌▐▌▐█▌.▐▌    ▐█▄▪▐█▐█▌▐█▄▄▌██▐█▌ ▐█▌·▐█▌.▐▌    ▐█▪·•▐█▄▄▌▐█•█▌██. ██ ▐█▌▐█▄▪▐█ ▐█▌·▐█▄▄▌▐█▄▪▐█
.▀▀▀  ▀█▄▀▪     ▀▀▀▀ ▀▀▀ ▀▀▀ ▀▀ █▪ ▀▀▀  ▀█▄▀▪    .▀    ▀▀▀ .▀  ▀▀▀▀▀▀• ▀▀▀ ▀▀▀▀  ▀▀▀  ▀▀▀  ▀▀▀▀ 

""")
            print("La palabra era")
            print(palabras)
            break

        # Si el usuario ingresa una letra que se encuentra en la palabra y no la ha ingresado antes,
        # reemplazar las rayas por la letra en todas las posiciones en las que se encuentra la letra
        # y aumentar el contador de aciertos.
        if letra in palabra and letra not in caracteres_puestos:
            posiciones = []
            pos = palabras.find(letra.lower())

            # Encontrar todas las posiciones en las que se encuentra la letra
            while pos != -1:
                posiciones.append(pos)
                pos = palabras.find(letra.lower(), pos + 1)

            # Reemplazar las rayas por la letra en las posiciones encontradas
            for item in posiciones:
                rayas[item] = letra

            print(posiciones)
            aciertos = aciertos + len(posiciones)

            # Limpiar la pantalla y mostrar un mensaje de que el usuario ha acertado
            os.system("clear")
            caracteres_puestos.append(letra)
            print("""
███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███░░░░░░▄▀░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░░░░░▄▀░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░████░░▄▀░░███████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░█████████████░░▄▀░░█████░░▄▀░░█████████░░▄▀░░█████████
█░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███████░░▄▀░░█████░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█████░░▄▀░░█████░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███████░░▄▀░░█████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█████░░▄▀░░█████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░░░███████░░▄▀░░█████░░▄▀░░░░░░▄▀░░█░░░░░░░░░░▄▀░░█████░░▄▀░░█████░░▄▀░░░░░░░░░░█░░░░░░░░░░▄▀░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█████████░░▄▀░░█████░░▄▀░░██░░▄▀░░█████████░░▄▀░░█████░░▄▀░░█████░░▄▀░░█████████████████░░▄▀░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░░░░░█████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░░░░░░░░░▄▀░░█████░░▄▀░░█████░░▄▀░░░░░░░░░░█░░░░░░░░░░▄▀░░█
█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░█████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█████░░▄▀░░█████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░░░█████░░░░░░█████░░░░░░██░░░░░░█░░░░░░░░░░░░░░█████░░░░░░█████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
            """)
            continue

        # Si el usuario ingresa una letra que ya había ingresado antes, mostrar un mensaje de error
        elif letra in caracteres_puestos:
            os.system("clear")
            print("""
███████████████████████████████████████████████████████████████████████████████
█▄─▄▄─█─▄▄▄▄██▀▄─████▄─▄███▄─▄▄─█─▄─▄─█▄─▄▄▀██▀▄─████▄─█─▄██▀▄─████▄─▄████▀▄─██
██─▄█▀█▄▄▄▄─██─▀─█████─██▀██─▄█▀███─████─▄─▄██─▀─█████▄─▄███─▀─█████─██▀██─▀─██
▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▀▀▀▀▄▄▄▀▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀
██████████████████████████████████████████████████
█▄─▄▄─█▄─██─▄█─▄▄▄▄█▄─▄█─▄▄▄▄█─▄─▄─█▄─▄▄─█─▄▄▄▄█░█
██─▄▄▄██─██─██▄▄▄▄─██─██▄▄▄▄─███─████─▄█▀█▄▄▄▄─█▄█
▀▄▄▄▀▀▀▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▀
""")
            continue

        # Si el usuario ingresa una letra que no se encuentra en la palabra, reducir las vidas
        # y mostrar un mensaje de que ha fallado
        else:
            os.system("clear")
            print("""
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░█████████░░░░░░█████████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░░░░░▄▀░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█
█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░█████████████░░▄▀░░█████░░▄▀░░█████████░░▄▀░░█████████
█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█████░░▄▀░░█████░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█████░░▄▀░░█████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░░░░░▄▀░░█░░░░░░░░░░▄▀░░█████░░▄▀░░█████░░▄▀░░░░░░░░░░█░░░░░░░░░░▄▀░░█
█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█████████░░▄▀░░█████░░▄▀░░█████░░▄▀░░█████████████████░░▄▀░░█
█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░░░░░░░░░▄▀░░█████░░▄▀░░█████░░▄▀░░░░░░░░░░█░░░░░░░░░░▄▀░░█
█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█████░░▄▀░░█████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░░░░░█████████░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░░░░░░░░░█████░░░░░░█████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
""")
            caracteres_puestos.append(letra)
            vida = vida -1
            continue

    # Si el usuario ha adivinado todas las letras, mostrar un mensaje de que ha ganado
    if aciertos == caracteres:
        os.system("clear")
        print(" ".join(rayas))
        print("""

oooooooooooo           oooo   o8o             o8o        .o8                  .o8                     
`888'     `8           `888   `"'             `"'       "888                 "888                     
 888          .ooooo.   888  oooo   .ooooo.  oooo   .oooo888   .oooo.    .oooo888   .ooooo.   .oooo.o 
 888oooo8    d88' `88b  888  `888  d88' `"Y8 `888  d88' `888  `P  )88b  d88' `888  d88' `88b d88(  "8 
 888    "    888ooo888  888   888  888        888  888   888   .oP"888  888   888  888ooo888 `"Y88b.  
 888         888    .o  888   888  888   .o8  888  888   888  d8(  888  888   888  888    .o o.  )88b 
o888o        `Y8bod8P' o888o o888o `Y8bod8P' o888o `Y8bod88P" `Y888""8o `Y8bod88P" `Y8bod8P' 8""888P' 
                                                                                                      
                                                                                                      
                                                                                                      

""")
        print("""

                                                                                                      .-'''-.     
                                                                                     _______         '   _    \   
   .                                                               _..._             \  ___ `'.    /   /` '.   \  
 .'|                                          .--./)             .'     '.            ' |--.\  \  .   |     \  '  
<  |                                         /.''\\             .   .-.   .           | |    \  ' |   '      |  ' 
 | |             __                         | |  | |      __    |  '   '  |    __     | |     |  '\    \     / /  
 | | .'''-.   .:--.'.         _              \`-' /    .:--.'.  |  |   |  | .:--.'.   | |     |  | `.   ` ..' /   
 | |/.'''. \ / |   \ |      .' |             /("'`    / |   \ | |  |   |  |/ |   \ |  | |     ' .'    '-...-'`    
 |  /    | | `" __ | |     .   | /           \ '---.  `" __ | | |  |   |  |`" __ | |  | |___.' /'                 
 | |     | |  .'.''| |   .'.'| |//            /'""'.\  .'.''| | |  |   |  | .'.''| | /_______.'/                  
 | |     | | / /   | |_.'.'.-'  /            ||     ||/ /   | |_|  |   |  |/ /   | |_\_______|/                   
 | '.    | '.\ \._,\ '/.'   \_.'             \'. __// \ \._,\ '/|  |   |  |\ \._,\ '/                             
 '---'   '---'`--'  `"                        `'---'   `--'  `" '--'   '--' `--'  `"                              

""")

# Iniciar el juego
if __name__ == "__main__":
    run()