# Откройте и прочитайте данные с файла lorum.txt, способом, который рассматривается в видео из пункта 1.

f = open('lorum.txt', 'r', encoding='utf-8')
print(f.read())
f.close()

f = open('lorum.txt', 'r', encoding='utf-8')
print(f.read(7))
print(f.read(7))
f.close()

f = open('lorum.txt', 'r', encoding='utf-8')
print(f.readline())
#print(f.readline())
f.close()

f = open('lorum.txt', 'r', encoding='utf-8')
for row in f:
    print(row)
f.close()

f = open('lorum.txt', 'r', encoding='utf-8')
for row in f:
    for letter in row:
        print(letter)
f.close()

f = open('lorum.txt', 'r', encoding='utf-8')
s = f.readlines()
print(s)
f.close()

f = open('lorum.txt', 'w', encoding='utf-8')
f.write('hello\n')
f.write('hello\n')
f.write('hello\n')
f.close()

f = open('lorum.txt', 'a+', encoding='utf-8')
f.write('hi\n')
f.write('hi\n')
f.write('hi\n')
s = f.readlines()
print(s)
f.close()
