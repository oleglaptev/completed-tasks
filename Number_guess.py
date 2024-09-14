from random import *


def is_valid(n, t):
    if n > t or n < 1:
        return False
    return True


def raund(a, b):
    if b < a:
        return 'Ваше число меньше загаданного, попробуйте еще разок', False
    elif b > a:
        return 'Ваше число больше загаданного, попробуйте еще разок', False
    else:
        return '', True

def game():
    print('Добро пожаловать в числовую угадайку')
    t = int(input('Выберите, до какой границы будет выбираться число '))
    a = randint(1, t)
    b = int(input('Введите число, которое мы загадали '))

    i = 1
    while not raund(a, b)[1]:
        i += 1
        if is_valid(b, t):
            print(raund(a, b)[0])
        else:
            i -= 1
            print(f'А может быть все-таки введем целое число от 1 до {t}?')
        b = int(input('Введите новое число '))
    print('Вы угадали, поздравляем!')

    print('Попыток:', i, '\nСпасибо, что играли в числовую угадайку. Еще увидимся...')


s = input('Н - начать новую игру, любая другая буква - выход из игры ')
while s == 'Н':
    game()
    s = input('Н - начать новую игру, любая другая буква - выход из игры ')
print('До встречи!')