import random
import os

def normalize(s):
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
# Este bloque de código se encarga de elegir una palabra aleatoria
    with open("./data.txt", "r", encoding="UTF-8") as f:
        lista_pal = list(f)
    palabras = random.choice(lista_pal)
    palabras = normalize(palabras)
    palabra = list(palabras.upper())
    palabra.pop(-1)

# Este bloque de código se encarga de contar los caracteres
    caracteres = len(palabra)
    aciertos = 0
    caracteres_puestos = []
    vida = 10
    rayas = []
    for i in range(len(palabra)):
        rayas.append("_")
    print(rayas)

# Este bloque de código de encarga de

    os.system("clear")

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

    while caracteres != aciertos:
        print(" ".join(rayas))
        print("Tienes", vida, "vidas")

        try:
            letra = input("Ingrese un cáracter porfavor: ").upper()
            if len(letra) > 1 or letra.isnumeric():
                raise TypeError("Solo se puede ingresar una única letra")
        
        except ValueError as ve:
            print(ve)
            continue

            
        if vida == 0:
            os.system("clear")
            print("PERDISTE")
            print("La palabra era")
            print(palabras)
            break
        if letra in palabra and letra not in caracteres_puestos:
            
            posiciones = []

            pos = palabras.find(letra.lower())

            while pos != -1:
                posiciones.append(pos)
                pos = palabras.find(letra.lower(), pos + 1)

            for item in posiciones:
                rayas[item] = letra

            print(posiciones)
            aciertos = aciertos + len(posiciones)
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
    

    if aciertos == caracteres:
        os.system("clear")
        print(" ".join(rayas))
        print("Felicidades")
        print("Has ganado")



if __name__ == "__main__":
    run()   