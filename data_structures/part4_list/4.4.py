#В предыдущей задаче должен был получиться список из букв. Используя методы списков: удалите из него последний элемент, сделайте реверсию списка.

c = ['a', 's', '1', 'a', '32', '23']
word =[]
number = []

for i in c:
    if i.isalpha():
        word.append(i)
    else:
        number.append(i)
print(word, number)

del word[2]
word.reverse()
print(word)