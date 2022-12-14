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