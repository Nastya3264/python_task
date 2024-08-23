# Руководство по [list comprehension]

# допустим, у нас есть список фруктов, где зафиксированы самые низкие и высокие цены на эти фрукты
# т.е. по сути это список списков :)
lst = [["apple", 55, 62], ["orange", 60, 74], ["pineapple", 140, 180], ["lemon", 80, 84]]

# выведем этот список для нагляности на экран, используя [list comprehension]
[print(el) for el in lst]
# ['apple', 55, 62]
# ['orange', 60, 74]
# ['pineapple', 140, 180]
# ['lemon', 80, 84]

# если мы хотим подсчитать среднюю цену на каждый из фруктов, то напишем что-то вроде
sumMiddle = 0
for el in lst:
    sumMiddle = (el[1] + el[2]) / 2
    print(sumMiddle)

# или можно сделать это одной строкой
[print((priceLow + priceHigh) / 2) for fruit, priceLow, priceHigh in lst]
# представьте, что наш список списков - это таблица из трёх столбцов
# и мы можем обращаться к столбцам, просто озаглавив их fruit, priceLow, priceHigh
# в цикле for, почти как перебор элементов словаря for key, value in d.items() :)

# поэтому, когда вы захотите прикинуть, сколько же, от и до, в среднем может стоить
# ваша фруктовая корзина, нужно будет посчитать среднее по каждой колонке
# вы можете сделать это примерно так
sumLow, sumHigh = 0, 0
for el in lst:
    sumLow += el[1]
    sumHigh += el[2]
sumLow /= len(lst)
sumHigh /= len(lst)
print(sumLow, sumHigh)

# или применить кунг-фу списковых выражений и обойтись парой строк :)
print(sum([priceLow for fruit, priceLow, priceHigh in lst]) / len(lst))
print(sum([priceHigh for fruit, priceLow, priceHigh in lst]) / len(lst))

# а где два принта, там и один :)
print(sum([priceLow for fruit, priceLow, priceHigh in lst]) / len(lst), sum([priceHigh for fruit, priceLow, priceHigh in lst]) / len(lst))


# Изменения:

# Чтобы не ограничиваться длиной строки в матрице, например
# ['apple', 55, 62, 49, ..., priceN]
# ['orange', 60, 74, 86, ..., priceN]
# ['pineapple', 140, 180, 192, ..., priceN]
# ['lemon', 80, 84, 79, ..., priceN]

# И соответственно, не плодить priceLow, priceHigh, ..., priceN можно слегка изменить код.
# Вместо этого:
# или можно сделать это одной строкой
# [print((priceLow + priceHigh) / 2) for fruit, priceLow, priceHigh in lst]

# используем Extended Iterable Unpacking (*args):
print( *[sum(price)/len(price) for fruit,*price in lst], sep='\n' )

# И вместо кучи print-ов:
## print(sum([priceLow for fruit, priceLow, priceHigh in lst]) / len(lst))"
## print(sum([priceHigh for fruit, priceLow, priceHigh in lst]) / len(lst))"
## ...
## print N sum

# тоже используем *args:
for i in range(1, len(lst[0])):
    print( sum([price[i] for [*price] in lst]) / len(lst) )