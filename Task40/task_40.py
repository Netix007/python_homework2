# Создайте программу для игры в "Крестики-нолики".

from os import system
from random import choice, randint

def player_name(n):  #ввод имени игрока
    name = ''
    while name == '':
        name = input(f'Введите имя Игрока {n}: ')
    return name

def intro():    #выбор варианта игры
    print('Добро пожаловать в игру "Крестик-нолик 2022"!!!')
    print('Выберите выриант игры')
    print('1 - Игра вдвоем', '2 - Игра с ботом', sep='\n')
    is_error = True
    while is_error:
        variant_game = input('Ваш выбор: ')
        try:
            int(variant_game)
            is_error = False
        except ValueError:
            is_error = True
            continue
        variant_game = int(variant_game)
        if not is_error and variant_game in [1, 2]:
            return variant_game
        else:
            is_error = True

def pole(list_cell):
    print(f'{name1} против {name2}\n')
    print('    1   2   3')
    print(f'1 |¯{list_cell[0]}¯|¯{list_cell[1]}¯|¯{list_cell[2]}¯|')
    print(f'2 |¯{list_cell[3]}¯|¯{list_cell[4]}¯|¯{list_cell[5]}¯|')
    print(f'3 |¯{list_cell[6]}¯|¯{list_cell[7]}¯|¯{list_cell[8]}¯|')
    print('   ¯¯¯¯¯¯¯¯¯¯¯ ')

def input_move(player_name, list_cell, cross_zero):
    is_error = True
    while is_error:
        text = input(f'Игрок {player_name} сделайте ход: ')
        try:
            [int(i)-1 for i in text.split()]
        except ValueError:
            print('введены недопустимые координаты (Пример корректного ввода: 2 1)')
            continue
        player_move = [int(i)-1 for i in text.split()]
        if len(player_move) == 2 and 0 <= player_move[0] <= 2 and 0 <= player_move[1] <= 2 :
            temp = 3 * player_move[0] + player_move[1]
            if list_cell[temp] == '¯':
                list_cell[temp] = cross_zero
                is_error = False
                break
            print('ячейка с такими координатами уже занята')
        else:
            print('ячейки с такими координатами не существует')
    return list_cell

def is_win(list_cell):  #проверка на победу
    diag1, diag2 = '', ''
    for i in range(3):
        col, row = '', ''
        for j in range(3):
            col += list_cell[3*j + i]
            row += list_cell[3*i + j]
            if i == j:
                diag1 += list_cell[4*i]
                diag2 += list_cell[2*i + 2]
        if col in 'XXX OOO' or row in 'XXX OOO':
            return True
    if diag1 in 'XXX OOO' or diag2 in 'XXX OOO':
        return True
    return False

def bot_move(list_cell, cross_zero):    #Ходы бота
    #s = [i for i in range(len(list_cell)) if list_cell[i] == '¯']
    #list_cell[choice(s)] = cross_zero
    list_cell[bot_nous(list_cell, cross_zero)] = cross_zero
    return list_cell

def bot_nous(list_cell, cross_zero):
    temp = cross_zero + '¯' + cross_zero*2 + '¯'
    diag1, diag2 = '', ''
    s = [i for i in range(len(list_cell)) if list_cell[i] == '¯']
    recomend_move = choice(s)
    for i in range(3):
        col, row = '', ''
        for j in range(3):
            col += list_cell[3*j + i]
            row += list_cell[3*i + j]
            if i == j:
                diag1 += list_cell[4*i]
                diag2 += list_cell[2*i + 2]
        if col in temp:
            recomend_move = i + 3*col.index('¯')
            return recomend_move
        elif row in temp:
            recomend_move = 3 * i + row.index('¯')
            return recomend_move        
    if diag1 in temp:
        recomend_move = 4*diag1.index('¯') 
    elif diag2 in temp:
        recomend_move = 2*diag2.index('¯') + 2
    return recomend_move


variant_game = intro()
list_cell = ['¯' for i in range(9)]
name1 = player_name(1)
if variant_game == 1:
    name2 = player_name(2)
else:
    name2 = 'Бот'
who_start = randint(1, 2)
if who_start != 1:
    name1, name2 = name2, name1

system('cls')
count = 1
print('   Ход №', count)
pole(list_cell)
if variant_game == 2 and name1 == 'Бот':
    list_cell = bot_move(list_cell, 'X')
else:
    list_cell = input_move(name1, list_cell, 'X')
flag = 'X'
while count <= 8 and not is_win(list_cell):
    count += 1
    system('cls')
    print('   Ход №', count)
    pole(list_cell)
    if variant_game == 2 and name2 == 'Бот':
        list_cell = bot_move(list_cell, 'O')
    else:
        list_cell = input_move(name2, list_cell, 'O')
    if is_win(list_cell):
        flag = 'O'
        break
    count += 1
    system('cls')
    print('   Ход №', count)
    pole(list_cell)
    if variant_game == 2 and name1 == 'Бот':
        list_cell = bot_move(list_cell, 'X')
    else:
        list_cell = input_move(name1, list_cell, 'X')
system('cls')
if is_win(list_cell):
    if flag == 'X':
        print(f'Игра завершена! Победил игрок {name1}! Потрачено ходов:', count)
    else:
        print(f'Игра завершена! Победил игрок {name2}! Потрачено ходов:', count)
else:
    print(f'Игра завершена! Победила дружба!')
pole(list_cell)
print('¯' + 'X'*2 + '¯')