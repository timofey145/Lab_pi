x1 = int(input("координата X1: "))
y1 = int(input("координата Y1: "))
x2 = int(input("координата X2: "))
y2 = int(input("координата Y2: "))

if  x1 > 0 and y1 > 0:          ## первая
    if x2 > 0 and y2 > 0:
        print("точки в первой четверти")
    elif not (x2 > 0 and y2 > 0):
        print("точки в разных четвертях")

elif x1 < 0 and y1 > 0:         ## вторая
    if x2 < 0 and y2 > 0:
        print("точки во второй четверти")
    elif not (x2 < 0 and y2 > 0):
        print("точки в разных четвертях")

elif x1 < 0 and y1 < 0:         ## третья
    if x2 < 0 and y2 < 0:
        print("точки в третьей четверти")
    else:
        print("точки в разных четвертях")

elif x1 > 0 and y1 < 0:
    if x2 > 0 and y2 < 0:
        print("точки в четвёртой четверти")
    else:
        print("точки в разных четрвертях")

elif x1 == 0 or y1 == 0 or x2 == 0 or y2 == 0:
    print("координаты не должны равнятся нулю")