#Найдите и скопируйте алгоритм бинарного поиска. Запустите код и попробуйте разобраться как он работает

def binary_search(lst, target):
    start = 0
    end = len(lst) - 1
    while(start <= end):
        mid = (start + end) // 2
        if(lst[mid] > target):
            end = mid - 1
        elif(lst[mid] < target):
            start = mid + 1
        else:
            return mid
    return None

numbers =[11, 23, 36, 47, 51, 66, 73, 83, 92]
target1 = 23
target2 = 70

print('число', target1, 'нашлось', binary_search(numbers, target1))
print('число', target2, 'нашлось', binary_search(numbers, target2))