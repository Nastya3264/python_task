# Задача
# Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов,
# и производит обратную операцию, получая исходный текст.
# Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
# В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

# Решение для конкретной последовательности
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
