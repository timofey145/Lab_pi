packets = input("ввод: ")

kol_packets = len(packets) ##количестов
if kol_packets < 5:
    print(" Длина строки должна быть не меньше 5! ")
    pass

count = 0       #не успешные
count_tek = 0
count_max = 0   #серия 0
for char in packets:
    if char == "0":
        count += 1

for char in packets:
    if char == "0":
        count_tek += 1
        if count_tek > count_max:
            count_max = count_tek

    elif char == "1":
        count_tek = 0

    else:
        print("в строке должны использоваться 0 и 1!")
        pass

procent = (count / kol_packets)*100

if procent < 1:
    quality = "Отличное качество"
elif procent < 5:
    quality =" Хорошее качество "
elif procent < 10:
    quality =" Удовлетворительное качество"
elif procent < 20:
    quality ="Плохое качество "
elif procent > 20:
    quality ="Критическое состояние сети "

print(f"{procent:.2f}")
print(f"Ввод: ")
print(packets)
print("Вывод:")
print(f"Общее количество пакетов: {kol_packets}")
print(f"Количество потерянных пакетов: {count}")
print(f"Длина самой длинной последовательности потерянных пакетов: {count_max}")
print(f"Процент потерь: {procent:.1f}%")
print(f"Качество связи: {quality}")





