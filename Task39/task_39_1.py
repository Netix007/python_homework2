# Создайте программу для игры с конфетами человек против человека.

from random import randint

def player_name(n):  #ввод имени игрока
    name = ''
    while name == '':
        name = input(f'Введите имя Игрока {n}: ')
    return name

def intro():    #выбор варианта игры
    print('Добро пожаловать в игру с конфетами!!!')
    print('Выберите выриант игры')
    print('1 - Игра вдвоем', '2 - Игра с ботом', '3 - Игра с супер-ботом', sep='\n')
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
        if not is_error and variant_game in [1, 2, 3]:
            return variant_game
        else:
            is_error = True
    
def recomendation(candies): #подсказки игроку 1
    if candies > 28:
        recomend = candies - ((candies // 29 ) * 29)
    else:
        recomend = candies
    if recomend != 0:
        print(f'Подсказка: для победы Игроку 1 необходимо взять {recomend} конфет')
    else:
        print(f'Подсказка: у Игрока 1 мало шансов на победу')

def moves_user(candies, player, need_help): #ходы пользователя
    if player == need_help:
        recomendation(candies)
    is_error = True
    while is_error:
        player_move = input(f'Осталось конфет: {candies}. Ход Игрока {player}: ')
        try:
            int(player_move)
            is_error = False
        except ValueError:
            is_error = True
            continue
        player_move = int(player_move)
        if not is_error and 0 < player_move <= candies and player_move <= 28:
            return player_move
        else:
            is_error = True

def moves_pc(candies, player, variant_of_game): #ходы бота
    if variant_of_game == 2:
        if candies >= 28:
            bot_move = randint(1, 28)
        else:
            bot_move = randint(1, candies)
        print(f'Осталось конфет: {candies}. Ход Игрока {player}: {bot_move}')
        return bot_move
    else:
        if candies > 28:
            bot_move = candies - ((candies // 29 ) * 29)
        else:
            bot_move = candies
        if bot_move != 0:
            print(f'Осталось конфет: {candies}. Ход Игрока {player}: {bot_move}')
            return bot_move
        else:
            print(f'Осталось конфет: {candies}. Ход Игрока {player}: {bot_move}')
            return randint(1, 28)


candies = 100
variant_of_game = intro()
name1 = player_name(1)
player1 = name1
if variant_of_game == 1:
    name2 = player_name(2)
elif variant_of_game == 2:
    name2 = 'Бот'
else:
    name2 = 'Супер-бот'
who_start = randint(1, 2)
if who_start != 1:
    name1, name2 = name2, name1
while candies != 0:
    if variant_of_game == 1:
        move_first = moves_user(candies, name1, player1)
    else:
        if name1 == player1:
            move_first = moves_user(candies, name1, player1)
        else:
            move_first = moves_pc(candies, name1, variant_of_game)
    candies -= move_first
    if candies == 0:
        print(f'Выиграл Игрок {name1}!!!')
        break
    if variant_of_game == 1:
        move_second = moves_user(candies, name2, player1)
    else:
        if name2 == player1:
            move_second = moves_user(candies, name2, player1)
        else:
            move_second = moves_pc(candies, name2 ,variant_of_game)
    candies -= move_second
    if candies == 0:
        print(f'Выиграл Игрок {name2}!!!')
        break
