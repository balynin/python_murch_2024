# Difference between modes a, a+, w, w+, and r+ in built-in open function?
# Попробуйте открыть файлы с разными значениями mode для чтения.
# Запишите любую информацию в файл с разными значениями mode для записи. Какую разницу при записи файла вы заметили?

#                   | r   r+   w   w+   a   a+
# ------------------|--------------------------
# read              | +   +        +        +
# write             |     +    +   +    +   +
# write after seek  |     +    +   +
# create            |          +   +    +   +
# truncate          |          +   +
# position at start | +   +    +   +
# position at end   |                   +   +

f = open('lorum.txt', 'r', encoding='utf-8')
s = f.readlines()
print(s)
f.close()

f = open('lorum.txt', 'r+', encoding='utf-8')
f.write('123\n')
s = f.readlines()
print(s)
f.close()

f = open('lorum.txt', 'w', encoding='utf-8')
#s = f.readlines()
f.write('456\n')
print(s)
f.close()

f = open('lorum.txt', 'w+', encoding='utf-8')
f.write('789\n')
s = f.readlines()
print(s)
f.close()

f = open('lorum.txt', 'a', encoding='utf-8')
#s = f.readlines()
f.write('101112\n')
print(s)
f.close()

f = open('lorum.txt', 'a+', encoding='utf-8')
s = f.readlines()
f.write('131415\n')
print(s)
f.close()