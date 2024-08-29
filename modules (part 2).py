# Задача 1
# Скачайте файл. В нём указан адрес другого файла, который нужно скачать с использованием модуля requests  и
# посчитать число строк в нём. Используйте функцию get для получения файла (имеет смысл вызвать метод strip к
# передаваемому параметру, чтобы убрать пробельные символы по краям).
# После получения файла вы можете проверить результат, обратившись к полю text. Если результат работы скрипта не
# принимается, проверьте поле url на правильность.
# Для подсчёта количества строк разбейте текст с помощью метода splitlines.
# В поле ответа введите одно число или отправьте файл, содержащий одно число.

# (1 способ)
# import requests
# url = 'https://stepik.org/media/attachments/course67/3.6.2/662.txt'
# r = requests.get(url)
# text_file = r.text.splitlines()
# print(text_file)
#
# count = 0
# for i in text_file:
#         count += 1
# print(count)
#
# # (2 способ)
# from requests import get
# with open('dataset_3378_2.txt') as file:
#         url = file.readline().strip()
# text = get(url).text.splitlines()
# print(text)
# print(len(text))

# Задача 2
# Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
# Первое слово в тексте последнего файла: "We".
# Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
# Все файлы располагаются в каталоге по адресу:
# https://stepik.org/media/attachments/course67/3.6.3/
# Загрузите содержимое последнего файла из набора, как ответ на это задание.

from requests import get
file = get('https://stepik.org/media/attachments/course67/3.6.3/699991.txt')
while not file.text.startswith('We'):
        file = get('https://stepik.org/media/attachments/course67/3.6.3/' + file.text.strip())
print(file.text)
