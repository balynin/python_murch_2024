# Дано целое число в диапазоне 100–999. Вывести строку-описание данного числа, например: 256 — «двести пятьдесят шесть», 814 — «восемьсот четырнадцать».

n = int(input('N  '))

from num2words import num2words
print(num2words(n, lang='ru'))

# n_div_100 = n // 100
# match n_div_100:
#     case 1:
#         print('сто ')
#     case 2:
#         print('двести ')
#     case 3:
#         print('тристо ')
#     case 4:
#         print('четыресто ')
#     case 5:
#         print('пятьсот ')
#     case 6:
#         print('шестьсот ')
#     case 7:
#         print('семьсот ')
#     case 8:
#         print('восемьсот ')
#     case 9:
#         print('девятьсот ')
#
#
# match n_div_100:
#     case 2:
#         print('двадцать ')
#     case 3:
#         print('тридцать ')
#     case 4:
#         print('сорок ')
#     case 5:
#         print('пятьдесят ')
#     case 6:
#         print('шестьдесят ')
#     case 7:
#         print('семьдесят ')
#     case 8:
#         print('восемьдесят ')
#     case 9:
#         print('девяносто ')
#
# match n_div_100:
#     case 10:
#         print('десять ')
#     case 11:
#         print('одинадцать ')
#     case 12:
#         print('двенадцать ')
#     case 13:
#         print('тринадцать ')
#     case 14:
#         print('четырнадцать ')
#     case 15:
#         print('пятнадцать ')
#     case 16:
#         print('шестнадцать ')
#     case 17:
#         print('семнадцать ')
#     case 18:
#         print('восемнадцать ')
#     case 19:
#         print('девятнадцать ')
#
# match n_div_100:
#     case 1:
#         print('один ')
#     case 2:
#         print('два ')
#     case 3:
#         print('три ')
#     case 4:
#         print('четыре ')
#     case 5:
#         print('пять ')
#     case 6:
#         print('шесть ')
#     case 7:
#         print('семь ')
#     case 8:
#         print('восемь ')
#     case 9:
#         print('девять ')
