# Solo querria decirte que este projecto, aunque aun es mejorable, me a supuesto mucho esfuerzo y te agradeceria se me pudieses dar algo de apoyo.
# Y te agradeceria si al encontrar algun error me lo pudieses decir en mi Twitter @Garlok_Dev(https://twitter.com/Garlok_Dev)

import time
from io import open
import random

#SESION ON
print()
print()
print()
print("         Hora a la que se abrio la sesion:       " + time.strftime("%H : %M : %S"))
print()

#BUCLES WHILE
bc = 1

#LOGO
print()
print()
print("          __    __              ________               ______   ")
print("         |  \  |  \            |        \             /      \  ")
print("         | ▓▓\ | ▓▓            | ▓▓▓▓▓▓▓▓            |  ▓▓▓▓▓▓\ ")
print("         | ▓▓▓\| ▓▓            | ▓▓__                | ▓▓___\▓▓ ")
print("         | ▓▓▓▓\ ▓▓            | ▓▓  \                \▓▓    \  ")
print("         | ▓▓\▓▓ ▓▓            | ▓▓▓▓▓                _\▓▓▓▓▓▓\ ")
print("         | ▓▓ \▓▓▓▓     __     | ▓▓_____      __     |  \__| ▓▓ ")
print("         | ▓▓  \▓▓▓    |  \    | ▓▓     \    |  \     \▓▓    ▓▓ ")
print("          \▓▓   \▓▓     \▓▓     \▓▓▓▓▓▓▓▓     \▓▓      \▓▓▓▓▓▓       V1.2")
print()                                                      
print()                                                   

print()
name = (input("Antes de nada podrias facilitarnos tu nombre: "))
print()

#Modo admin
if name == "admin" or name == "Admin" or name == "ADMIN":
    admin = input("Hola " + name + ". ¿Quieres activar el modo administrador? [Y/N]: ")
    if admin == "Y" or admin == "y":
        print()
        print("Modo administrador activado")
        print("¿Si quieres informarte mas sobre el modo administrado y sus comandos tipea 'admin comand' en N.E.S?")
        print()
    else:
        print()
        pass 
else:
    print()
    pass

#BUCLE
while bc == 1:
    nes = input(">NES<: ")

    #HELP
    if nes == "help" or nes == "Help" or nes == "HELP":
        print()
        print("     N.E.S es un programa que te acompaña en tu pc.")
        print("     Puedes hacer muchas cosas con N.E.S. ")
        print("     Este programa es un amigo en tu pc.")
        print("     N.E.S esta basado en MS-DOS, el lenguaje de Windows")
        print()
        print("     Para empezar te proporcionare los comandos de N.E.S")
        print()
        print("     exit : Salir de N.E.S")
        print("     start :  Empezar N.E.S")
        print()
        print("     Puedes consultar los comandos correspondientes en https://Garlok-Dev.github.io")
        print("     o tipeando en N.E.S 'comandos'")
        print()

    #SESION OFF
    elif nes == "exit" or nes == "Exit" or nes == "EXIT" or nes == "adios" or nes == "Adios" or nes == "ADIOS" or nes == "salir" or nes == "Salir" or nes == "SALIR":
        print()
        ext = input("¿Estas seguro de que quieres salir? [S/N]: ")
        print()
        if ext == "Si" or ext == "si" or ext == "SI" or ext == "S" or ext == "s":
            print()
            print("         Adios " + name + ". Espero volver a verte pronto :)")
            print()
            print("         Hora a la que se cerro la sesion:       " + time.strftime("%H : %M : %S"))
            print()
            print()
            break
        else:
            continue

    #C0M4ND2
    elif nes == "comandos" or nes == "Comandos" or nes == "COMANDOS":
        print()
        print("Hola")
        print("Adios")
        print("¿Que hora es?")
        print("¿Que dia es hoy?")
        print("Salir")
        print("Admin Comand [Se necesita activar el modo administrador para ejecutar este comando]")
        print("Activar modo calculadora")
        print("Random")
        print("Juego")
        print()

    #Comandos de Administrador
    elif nes == "admin comand" or nes == "Admin Comand" or nes == "Admin comand" or nes == "admin Comand" or nes == "ADMIN COMAND":
        if name == "admin":
            if admin == "Y" or nes == "y":
                print()
                print("")
                print()
            else:
                print()
                print("No tienes activado el modo administrador")
                admin = input("¿Quieres activarlo? [Y/N]: ")
                print()
        else:
            print()
            print("No eres el administrador")
            print("Para serlo, al iniciar N.E.S escribe 'admin' cuando te pregunten tu nombre.")
            print()


    #C0MU1C4C10N
    elif nes == "hola" or nes == "Hola" or nes == "HOLA":
        print()
        como_estas = input("Hola " + name + ", ¿como estas?: ")
        print()
        if como_estas == "bien":
            print("Me alegro " + name)
            print()
        if como_estas == "mal" or como_estas == "Mal" or como_estas == "MAL":
            mal = input("Lo siento. ¿Quieres desahogarte conmigo?: ")
            if mal == "no" or mal == "No" or mal == "NO":
                print()
                print("Vale, te comprendo. Algunas cosas son mejores pasarlas solos. Animo " + name + " :)")
                print()
                continue
            if mal == "si" or mal == "Si" or mal == "SI":
                print()
                input("Claro, cuentame " + name + ": ")
                print()
                print("Tranquilo/a " + name + ", todo se supera. Confio en ti guapo/a :)")
                print()
        
    elif nes == "¿que hora es?" or nes == "¿Que hora es?" or nes == "¿QUE HORA ES?":
        print()
        print("Son las " + time.strftime("%H : %M"))
        print()

    elif nes == "¿que dia es hoy?" or nes == "¿Que dia es hoy?" or nes == "¿QUE DIA ES HOY?":
        print()
        print("Hoy es " + time.strftime("%D"))
        print()

    elif nes == "gracias" or nes == "Gracias" or nes == "GRACIAS":
        print()
        print("Denada " + name)
        print()

    elif nes == "Activa modo calculadora" or nes == "activa modo calculadora" or nes == "calculadora" or nes == "Calculadora" or nes == "cal" or nes == "Activa Modo Calculadora" or nes == "Activar modo calculadora" or nes == "activar modo calculadora" or nes == "Activar Modo Calculadora":
        print()
        print("¿Que operacion desea realizar?")
        print()
        print("sumar = +")
        print("restar = -")
        print("multiplicar = *")
        print("dividir = /")
        print("elevar = **")
        print()
        cal = input("¿Que operacion vas a hacer?: ")
        print()
        if cal == "sumar" or cal == "Sumar" or cal == "SUMAR" or cal == "+":
            ns1 = int(input("Dime un numero: "))
            ns2 = int(input("Dime otro numero: "))
            print()
            rs = str(ns1 + ns2)
            print("El resultado es " + rs)
            print()
        elif cal == "restar" or cal == "Restar" or cal == "RESTAR" or cal == "-":
            nr1 = int(input("Dime un numero: "))
            nr2 = int(input("Dime otro numero: "))
            print()
            rr = str(nr1 - nr2)
            print("El resultado es " + rr)
            print()
        elif cal == "multiplicar" or cal == "Multiplicar" or cal == "MULTIPLICAR" or cal == "*":
            nm1 = int(input("Dime un numero: "))
            nm2 = int(input("Dime otro numero: "))
            print()
            rm = str(nm1 * nm2)
            print("El resultado es " + rm)
            print()
        elif cal == "dividir" or cal == "Dividir" or cal == "DIVIDIR" or cal == "/":
            nd1 = int(input("Dime un numero: "))
            nd2 = int(input("Dime otro numero: "))
            print()
            rd = str(nd1 / nd2)
            print("El resultado es " + rd)
            print()
        elif cal == "elevar" or cal == "Elevar" or cal == "ELEVAR" or cal == "**":
            ne1 = int(input("Dime un numero: "))
            ne2 = int(input("Dime otro numero: "))
            print()
            re = str(ne1 ** ne2)
            print("El resultado es " + re)
            print()

    elif nes == "random" or nes == "Random" or nes == "RANDOM" or nes == "ran" or nes == "Ran" or nes == "Aleatorio" or nes == "aleatorio" or nes == "dime un numero aleatorio" or nes == "Dime un numero aleatorio":
        ran = random.randint(0, 100000000)
        print()
        print("Un numero aleatorio entre 0 y 100000000 es = " + ran)
        print()

    elif nes == "juego" or nes == "Juego" or nes == "JUEGO" or nes == "jugar" or nes == "Jugar" or nes == "JUGAR":
        print()
        print("1: Piedra, papel o tijeras")
        print()
        gam = input("Elige un juego: ")
        print()
        if gam == "1" or gam == "piedra, papel o tijera" or gam == "Piedra, Papel o Tijeras":
            print("1: Piedra")
            print("2: Papel")
            print("3: Tijeras")
            print("")
            gam = input("Elije: ")
            print()
            ppt = random.randint(1, 3)
            if ppt == 1:
                print("N.E.S ha sacado > Piedra <")
                print()
                if gam == "1" or gam == "piedra" or gam == "Piedra" or gam == "PIEDRA":
                    print("Habeis empatado")
                    print()
                    pass
                elif gam == "2" or gam == "papel" or gam == "Papel" or gam == "PAPEL":
                    print("N.E.S ha perdido >:(")
                    print()
                    pass
                elif gam == "3" or gam == "tijeras" or gam == "Tijeras" or gam == "TIJERAS":
                    print(name + " ha perdido \^o^/")
                    print()
                    pass
                
            elif ppt == 2:
                print("N.E.S ha sacado > Papel <")
                print()
                if gam == "1" or gam == "piedra" or gam == "Piedra" or gam == "PIEDRA":
                    print(name + " ha perdido \^o^/")
                    print()
                    pass
                elif gam == "2" or gam == "papel" or gam == "Papel" or gam == "PAPEL":
                    print("Habeis empatado")
                    print()
                    pass
                elif gam == "3" or gam == "tijeras" or gam == "Tijeras" or gam == "TIJERAS":
                    print("N.E.S ha perdido >:(")
                    print()
                    pass
            
            elif ppt == 3:
                print("N.E.S ha sacado > Tijeras <")
                print()
                if gam == "1" or gam == "piedra" or gam == "Piedra" or gam == "PIEDRA":
                    print("N.E.S ha perdido >:(")
                    print()
                    pass
                elif gam == "2" or gam == "papel" or gam == "Papel" or gam == "PAPEL":
                    print(name + " ha perdido \^o^/")
                    print()
                    pass
                elif gam == "3" or gam == "tijeras" or gam == "Tijeras" or gam == "TIJERAS":
                    print("Habeis empatado")
                    print()
                    pass
        
