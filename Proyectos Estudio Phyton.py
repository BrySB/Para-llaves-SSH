###### EN ESTE ARCHIVO ESTARÉ CREANDO UNOS VIDEOJUEGOS PARA APRENDER HERRAMIENTAS BÁSICAS DEL LENGUAJE PYTHON #####

### Primer reto: 
# MADLIBS. Son en esencia un texto que completa una oración según unas palabras que se le pidan a un usuario con anterioridad.

from random import randint, random


to = input("Para: ")
name = input("De: ")
verb1 = input("Escribe un verbo: ")
verb2 = input("Escribe otro verbo: ")
adj1 = input("Escribe un estado de ánimo: ")
adj2 = input("Escribe un elogio: ")
adj3 = input("Escribe un defecto: ")

madlib = f"Hola, {to}. Te saluda {name}. Te escribo porque desde hace un par de meses no hago más que {verb1} de mi {adj1}. No puedo olvidar lo {adj2} que \
siempre fuiste. Espero algún día puedas volver a {verb2} junto a la {adj3} de tu mamá."

print(madlib)



import random
jenga = random.randint(1,57)

print(random.randint(1,57))

#Tengo que hacer los juegos de adivinar el número

# The Paper, Rock, Scissors Game
import random

import random

def play():
    user = input("Elige 'p' para piedra, 'r' para roca o 't' para tijeras.\n")
    computer = random.choice(['p','r','t'])

    if user == computer:
        return f'Es un empate. La computadora también ha elegido {computer}'
        # print(f'Has empatado, la computadora también ha elegido {computer}.')

    if is_win(user, computer):
        return f'¡Ganaste! La computadora ha elegido {computer}'
        # print(f'Has ganado, la computadora ha elegido {computer}.')

    return f'Mejor suerte para la próxima. La computadora ha elegido {computer}'
    # print(f'Mejor suerte a la próxima, la computadora ha elegido {computer}.')

def is_win(player, opponent):
    # Existen jerarquías para determinar el ganador: r>t t>p p>r
    if (player == 'r' and opponent == 't') or (player == 't' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())