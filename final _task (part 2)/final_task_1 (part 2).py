# Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча
# и выводит на стандартный вывод сводную таблицу результатов всех матчей.
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
# Формат ввода следующий:
# В первой строке указано целое число n — количество завершенных игр.
# После этого идет n строк, в которых записаны результаты игры в следующем формате:
# Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
# Вывод программы необходимо оформить следующим образом:
# Команда:Всего_игр Побед Ничьих Поражений Всего_очков
# Порядок вывода команд произвольный.

# (1 способ)
n = int(input())
d = {}

for i in range(n):
    lst = input().split(';')
    if lst[0] not in d.keys():
        d[lst[0]] = [0, 0, 0, 0, 0]
    if lst[2] not in d.keys():
        d[lst[2]] = [0, 0, 0, 0, 0]
    if int(lst[1]) > int(lst[3]):
        d[lst[0]] = [x + y for x, y in zip(d[lst[0]], [1, 1, 0, 0, 3])]
        d[lst[2]] = [x + y for x, y in zip(d[lst[2]], [1, 0, 0, 1, 0])]
    elif int(lst[1]) < int(lst[3]):
        d[lst[0]] = [x + y for x, y in zip(d[lst[0]], [1, 0, 0, 1, 0])]
        d[lst[2]] = [x + y for x, y in zip(d[lst[2]], [1, 1, 0, 0, 3])]
    else:
        d[lst[0]] = [x + y for x, y in zip(d[lst[0]], [1, 0, 1, 0, 1])]
        d[lst[2]] = [x + y for x, y in zip(d[lst[2]], [1, 0, 1, 0, 1])]

for key, value in d.items():
    print(f"{key}:{' '.join(str(x) for x in value)}") # конвертируем список в строку через пробел


# (2 способ)
def command(c, res):
    if c not in dct:
        dct[c] = [0, 0, 0, 0, 0]
    dct[c] = [
        dct[c][0] + 1,
        dct[c][1] + 1 if res == 3 else dct[c][1],
        dct[c][2] + 1 if res == 1 else dct[c][2],
        dct[c][3] + 1 if res == 0 else dct[c][3],
        dct[c][4] + res
    ]

dct = {}
for i in range(int(input())):
    c1, g1, c2, g2 = input().split(';')
    g1 = int(g1)  # Преобразуем g1 в целое число
    g2 = int(g2)  # Преобразуем g2 в целое число
    command(c1, 3 if g1 > g2 else 1 if g1 == g2 else 0)
    command(c2, 3 if g2 > g1 else 1 if g1 == g2 else 0)

for c in dct:
    print('{}:{} {} {} {} {}'.format(c, *dct[c]))