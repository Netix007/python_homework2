# Напишите программу, удаляющую из текста все слова, содержащие "абв".

s = [i for i in input('Введите текст: ').split() if 'абв' not in i]

print(' '.join(s))