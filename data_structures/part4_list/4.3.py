c = ['a', 's', '1', 'a', '32', '23']
word =[]
number = []

for i in c:
    if i.isalpha():
        word.append(i)
    else:
        number.append(i)
print(word, number)