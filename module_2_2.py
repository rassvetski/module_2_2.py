first = int(input('Введите число один:'))
second = int(input('Введите число два:'))
third = int(input('Введите число три:'))
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
elif first != second != third:
    print(0)
