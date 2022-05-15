# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.

def archiving(s): #сжатие
    result = ''
    while len(s) != 0:
        count = 1
        a = s[0]
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                count += 1
            else:
                s = s[i+1:]
                break
        else:
            s = ''
        result += str(count) + a
    return result

def unarchiving(s): #распаковка
    result = ''
    while len(s) != 0:
        for i in range(len(s)):
            if not s[i].isdigit():
                result += s[i]*int(s[:i])
                s = s[i+1:]
                break
    return result

print('1 - сжатие данных', '2 - восстановление данных', sep='\n')
variant = ''
while variant not in ['1', '2']:
    variant = input('Ваш выбор: ')

if variant == '1':
    txt = open("unarch.txt", 'r')
    s = txt.readline()
    txt.close()
    txt = open("arch.txt", 'w')
    txt.write(archiving(s))
    txt.close()
else:
    txt = open("arch.txt", 'r')
    s = txt.readline()
    txt.close()
    txt = open("unarch.txt", 'w')
    txt.write(unarchiving(s))
    txt.close()        

