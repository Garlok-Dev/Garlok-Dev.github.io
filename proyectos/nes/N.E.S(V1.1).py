import time
import pandas as pd

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
print("          \▓▓   \▓▓     \▓▓     \▓▓▓▓▓▓▓▓     \▓▓      \▓▓▓▓▓▓       V1.1")
print()                                                      
print()                                                   

print()
name = (input("Antes de nada podrias facilitarnos tu nombre: "))
print()

#Modo admin
if name == "admin" or name == "Admin":
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
    if nes == ["help" or nes == "Help"]:
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
    elif nes == "exit" or nes == "Exit":
        print()
        print("         Adios " + name + ". Espero volver a verte pronto :)")
        print()
        print("         Hora a la que se cerro la sesion:       " + time.strftime("%H : %M : %S"))
        print()
        print()
        break
    elif nes == "adios" or nes == "Adios" or nes == "salir" or nes == "Salir":
        print()
        print("         Adios " + name + ". Espero volver a verte pronto :)")
        print()
        print("         Hora a la que se cerro la sesion:       " + time.strftime("%H : %M : %S"))
        print()
        print()
        break

    #C0M4ND2
    if nes == "comandos" or nes == "Comandos":
        print()
        print("Hola")
        print("Adios")
        print("¿Que hora es?")
        print("¿Que dia es hoy?")
        print("Salir")
        print("Adios")
        print("Admin Comand [Se necesita activar el modo administrador para ejecutar este comando]")
        print()

    #Comandos de Administrador
    if nes == "admin comand" or nes == "Admin Comand" or nes == "Admin comand" or nes == "admin Comand":
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
    if nes == "hola" or nes == "Hola":
        print()
        como_estas = input("Hola " + name + ", ¿como estas?: ")
        if como_estas == "bien":
            print()
            print("Me alegro " + name)
            print()
        if como_estas == "mal" or como_estas == "Mal":
            print()
            mal = input("Lo siento. ¿Quieres desahogarte conmigo?: ")
            if mal == "no" or mal == "No":
                print()
                print("Vale, te comprendo. Algunas cosas son mejores pasarlas solos. Animo " + name + " :)")
                print()
                continue
            if mal == "si" or mal == "Si":
                print()
                input("Claro, cuentame " + name + ": ")
                print()
                print("Tranquilo/a " + name + ", todo se supera. Confio en ti guapo/a :)")
                print()
        
    if nes == "¿que hora es?" or nes == "¿Que hora es?":
        print()
        print("Son las " + time.strftime("%H : %M"))
        print()

    if nes == "¿que dia es hoy?" or nes == "¿Que dia es hoy?":
        print()
        print("Hoy es " + time.strftime("%D"))
        print()

    if nes == "gracias" or nes == "Gracias":
        print()
        print("Denada " + name)
        print()


        