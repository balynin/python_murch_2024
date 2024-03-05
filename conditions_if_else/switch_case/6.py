# Реализуйте программу калькулятор. На вход подается три значения: первое число, второе число и операция( *, /, + или -) . На выходе должны получить число, после выполнения операции.

num1 = float(input())
oper = str(input())
num2 = float(input())

match oper:
    case '*':
        print(num1 * num2, end='')
    case '/':
        print(num1 // num2, end='')
    case '+':
        print(num1 + num2, end='')
    case '-':
        print(num1 - num2, end='')
