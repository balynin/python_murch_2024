# Найти все простые числа от 2 до 50

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
a = 2
n = 50
res = [i for i in range(a, n) if is_prime(i)]
print(res)