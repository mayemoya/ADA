#Primera parte del proyecto integrador, dar la bienvenida con el nombre del jugador
"""print("Hola, ¿cuál es tu nombre?")
nombre = input()
print("Bienvenido/a, {}!".format(nombre))"""


#Segunda parte, importar libreria readchar que funciona para leer los caracteres del teclado.
#Escribir un programa que corra un bucle infinito leyendo e imprimiento las teclas y sólo 
#terminará cuando se presione la tecla ↑ indicada como UP
import readchar
import keyboard


while True:
    tecla = readchar.readkey()
    print(f"Tecla presionada: {tecla}")
    if keyboard.is_pressed('UP'): 
        print("Tecla UP presionada. Saliendo del programa.")
        break



