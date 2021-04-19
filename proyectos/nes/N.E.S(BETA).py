import time

#SESION ON
print()
print()
print()
print("         Hora a la que se abrio la sesion:       " + time.strftime("%H : %M : %S"))
print()

#BUCLE WHILE
on = 0

# def e404():
#     print()
#     print("     '" + nes + "'" + " no es un comando de N.E.S")
#     print()

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
print("          \▓▓   \▓▓     \▓▓     \▓▓▓▓▓▓▓▓     \▓▓      \▓▓▓▓▓▓  ")
print()                                                      
print()                                                   

#BUCLE
while on == 0:
    nes = input(">NES<: ")

    #HELP
    if nes == "help":
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

    elif nes == "exit":
        #SESION OFF
        print()
        print()
        print("         Hora a la que se cerro la sesion:       " + time.strftime("%H : %M : %S"))
        print()
        print()
        break

    #START N.E.S
    elif nes == "start":
        print()
        print("     Hola soy Garlok Dev y acabas de iniciar N.E.S")
        print()
        print("     ¿Que que es N.E.S?, te preguntaras.")
        print("     Pues N.E.S son las siglas de [N]o [E]stas [S]olo.")
        print()
        print("     Este programa es una IA la cual fue desarrollada con el fin de")
        print("     sustituir el projecto fallido que es Cortana.")
        print()
        print("     Puedes consultar los comandos correspondientes en https://Garlok-Dev.github.io")
        print()
        print()