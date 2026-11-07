num1 = (float(input("предыдущие: ")))
num2 = (float(input("текущие: ")))

def view_result():
    print("ввод:")
    print(num1)
    print(num2)
    print("вывод:")
    print("Предыдущее       Текущее        Использовано       К оплате       Ср.цена m^3")
    print(f"{num1}           {num2}           {res}           {sum_all:.2f}$       {sum_sr:.2f}")


if num2 >= num1:
    res = num2 - num1
else:
    res = (10000 - num1) + num2

sum_all = 0

if res <= 300:
    sum_all = 21.0
    sum_sr = sum_all / res
    view_result()

elif res <= 600:
    sum_all = 21.0
    sum_all += (res -300)*0.06
    sum_sr = sum_all/res
    view_result()

elif res <= 800:
    sum_all = 21.0
    sum_all += (300*0.06) + (res- 600) * 0.04
    sum_sr = sum_all/res
    view_result()

elif res > 800:
    sum_all = 21.0
    sum_all += (300*0.06) + (200*0.04) + (res-800)* 0.025
    sum_sr = sum_all/res
    view_result()



