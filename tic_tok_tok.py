import time

from termcolor import colored
from os import system
from time import sleep
import random

bord = [1, 2, 3, 4, 5, 6, 7, 8, 9]
win = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]


def print_bord():
    for i in enumerate(bord, 1):
        print(i[1], '\t', sep='', end='')
        if i[0] % 3 == 0:
            print()
    print()


def mov(m):
    if m % 2 == 0:
        return colored('x', 'red')
    return colored('o', 'blue')


def edit_bord(move1, y):
    bord[move1 - 1] = y


def check_win(y, b):
    for i in win:
        if b[i[0] - 1] == b[i[1] - 1] == b[i[2] - 1] == y:
            return True
    return False


def sys_win(y):
    for i in [i for i in bord if isinstance(i, int)]:
        bord[i - 1] = y
        b = bord.copy()
        bord[i - 1] = i
        if check_win(y, b):
            return i


def mov_sys():
    if (w := sys_win(colored('o', 'blue'))) is not None:
        return w

    if (e := sys_win(colored('x', 'red'))) is not None:
        return e

    for i in [[1, 3, 9, 7], [5], [2, 6, 8, 4]]:
        random.shuffle(i)
        for j in i:
            if j in bord:
                return j


def starting(choice):
    s = 3
    players = ('You' if choice == 1 else 'plyer 1', 'computer' if choice == 1 else 'plyer 2')
    while s != 0:
        system('cls')
        print(f"{players[0]}: {colored('x', 'red')}\n"
              f"{players[1]}: {colored('o', 'blue')}")
        print(f'Starting the game:({s})')
        sleep(1)
        s -= 1


def get_choice():
    """getting the choice"""
    print(' 1) Solitaire game\n'
          ' 2) Double game\n'
          ' 3) Exit')
    while True:
        choice = input('your choice:')
        if choice not in ['1', '2', '3']:
            print(f'{colored("wrong!", "red")} try again (1-3)')
            continue
        return int(choice)


def tic_tok_tok():
    if (choice := get_choice()) != 3:
        starting(choice)
        m = 0
        while m <= 8:
            system('cls')
            y = mov(m)
            move = -1
            try:
                if choice == 1:  # Playing with the computer
                    if y == colored('x', 'red'):
                        print_bord()
                        move = int(input(f'player move:'))
                    else:
                        move = mov_sys()

                elif choice == 2:  # Playing with others
                    print_bord()
                    move = int(input(f'player {y} move:'))

                if move not in bord:
                    raise ValueError('wrong! try again')

            except ValueError:
                print("wrong! try again")
                time.sleep(2)
                continue

            edit_bord(move, y)

            if check_win(y, bord):
                print('_____', y, colored('won', 'green'), '_____')
                print_bord()
                break
            m += 1

        else:
            system('cls')
            print('_____', colored('alike', 'yellow'), '_____')
            print_bord()
    # --------------------------------------------------
    while True:
        a = input("you want to exit the gami? (y/n)")
        if a == 'n':
            bord.clear()
            bord.extend([1, 2, 3, 4, 5, 6, 7, 8, 9])
            system('cls')
            tic_tok_tok()
        elif a == 'y':
            break
        else:
            print('wrong! try again\n')
            continue


tic_tok_tok()
