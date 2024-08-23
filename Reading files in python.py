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

