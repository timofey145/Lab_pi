n = int(input("введите n: " ))  ##высота
m = int(input("введите m: " ))  ##ширина
print("ПРЯМОУГОЛЬНИК 5x10:")
for i in range(n):      ##прямоугольник
    print("#" * m)

print("ПРАВЫЙ ТРЕУГОЛЬНИК: ")

count = 1               ##треугольник
for i in range(n):
    print( "#" * count )
    count += 1

print("РАМКА 5*10:")
print( "#" * m )
for i in range(n - 2):
    res = m - 2
    print("#" + " " * res + "#")
print( "#" * m )




