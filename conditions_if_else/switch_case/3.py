# Даны два целых числа: D (день) и M (месяц), определяющие правильную дату невисокосного года. Вывести значения D и M для даты, следующей за указанной.

d = int(input('D  '))
m = int(input('M  '))
data = ["311","292","313","304","315","306","317","318","309","3010","3011","3112"]
if str(d) + str(m) in data:
    d = 0
    m += 1
    if m == 12:
        m = 1
print(d+1, m)