number = input("Введите номер карты: ")
n = len(number)

total = 0           #Алгоритм Луна
count = 0
for ch in number:
    num = int(ch)
    if (n - count) % 2 == 0:
        num = num * 2
        if num > 9:
            num = num - 9
    total = total + num
    count = count + 1


start = int(number[0:2])

if total % 10 != 0:             #Проверяем сумму и определяем тип карты
    print("INVALID")

elif n == 15 and (start == 34 or start == 37):
    print("American Express")

elif n == 16 and 51 <= start <= 55:
    print("MasterCard")

elif (n == 13 or n == 16) and number[0] == "4":
    print("Visa")

else:
    print("INVALID")