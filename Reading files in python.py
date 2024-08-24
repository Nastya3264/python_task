# Задача 1
# Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов,
# и производит обратную операцию, получая исходный текст.
# Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
# В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

# Решение для конкретной последовательности
def task_1_1():
    sequence = 'a3b21c1'
    digits = set('1234567890')
    number = ''
    letter = sequence[0]
    answer = ''

    for symbol in sequence[1:]:
        if symbol in digits:
            number += symbol
        else:
            answer += letter * int(number)
            letter = symbol
            number = ''
    answer += letter * int(number)

# Решение для данного файла
def task_1_2():
    with open('dataset_3363_2.txt', encoding='utf-8') as file:
        sequence = file.readline().strip()
    digits = set('1234567890')
    number = ''
    letter = sequence[0]
    answer = ''

    for symbol in sequence[1:]:
        if symbol in digits:
            number += symbol
        else:
            answer += letter * int(number)
            letter = symbol
            number = ''
    answer += letter * int(number)

    with open('dataset_3363_2.txt', 'a') as file:
      file.write(answer)

# Задача 2
# Недавно мы считали для каждого слова количество его вхождений в строку.
# Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.
# Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки)
# и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько,
# вывести лексикографически первое (можно использовать оператор < для строк).
# В качестве ответа укажите вывод программы, а не саму программу.
# Слова, написанные в разных регистрах, считаются одинаковыми.

def task_2():
    d = {}

    with open('dataset_3363_3.txt') as file:
        for line in file:
            line = line.lower()
            for word in line.split():
                if word not in d:
                    d[word] = 1
                else:
                    d[word] += 1

    max_quantity = 1
    # переменная счетчик с макс.кол-вом

    for key, value in d.items():
        current_quantity = d[key]
        if current_quantity > max_quantity:
            max_quantity = current_quantity
            word_with_max_quantity = key

    with open('dataset_3363_3.txt', 'a') as file:
        most_popular = (word_with_max_quantity + ' ' + str(max_quantity))
        file.write(most_popular)

# Задача 3
# Имеется файл с данными по успеваемости абитуриентов.
# Он представляет из себя набор строк, где в каждой строке записана следующая информация:
# Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
# Поля внутри строки разделены точкой с запятой, оценки — целые числа.
# Напишите программу, которая считывает исходный файл с подобной структурой и для каждого абитуриента
# записывает его среднюю оценку по трём предметам на отдельной строке,
# соответствующей этому абитуриенту, в файл с ответом. Также вычислите средние баллы по математике,
# физике и русскому языку по всем абитуриентам и добавьте полученные значения, разделённые пробелом,
# последней строкой в файл с ответом. В качестве ответа на задание прикрепите полученный файл со средними оценками
# по каждому ученику и одной строкой со средними оценками по трём предметам.

def task_3():
    average_sc_lst = []
    sum_score_math = 0
    sum_score_rus = 0
    sum_score_physics = 0
    n = 0

    with open("dataset_3363_4.txt", "r", encoding='utf-8') as in_f:
        for line in in_f:
            name, *scores = line.strip().split(';')  # name - строка, scores - список из чисел (* - переменное число переменных)
            scores = [int(score) for score in scores]
            average_sc_lst.append(sum(scores) / len(scores))
            sum_score_math += scores[0]
            sum_score_rus += scores[1]
            sum_score_physics += scores[2]
            n += 1
    average_math = sum_score_math / n
    average_rus = sum_score_rus / n
    average_physics = sum_score_physics / n

    with open('dataset_3363_4_output.txt', 'w') as out_f:
        for score in average_sc_lst:
            out_f.write(str(score) + '\n') # запишем каждый элемент списка в отдельной строке
        out_f.write(f"{average_math} {average_rus} {average_physics}")
        # f-string - форматированная строка (подставляет переменные в строку с помощью фигурных скобок)

task_3()