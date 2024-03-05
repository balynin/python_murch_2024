# Дан номер месяца — целое число в диапазоне 1–12 (1 — январь, 2 — февраль и т. д.). Определить количество дней в этом месяце для невисокосного года.


k = int(input("порядковый номер месяца  "))
match k:
    case 1:
        print('31')
    case 2:
        print('29')
    case 3:
        print('31')
    case 4:
        print('30')
    case 5:
        print('31')
    case 6:
        print('30')
    case 7:
        print('31')
    case 8:
        print('30')
    case 9:
        print('31')
    case 10:
        print('30')
    case 11:
        print('31')
    case 12:
        print('30')
    case _:
        print('ошибка')

