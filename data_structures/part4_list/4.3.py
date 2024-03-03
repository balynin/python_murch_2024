#Дан список [«a», «s», «1», «a», «32», «23»]. Разбейте его на два списка: только с буквами и только с числами.

c = ['a', 's', '1', 'a', '32', '23']
word =[]
number = []

for i in c:
    if i.isalpha():
        word.append(i)
    else:
        number.append(i)
print(word, number)