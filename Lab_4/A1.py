import random
import time

N = random.randint(2, 9)
correct = 0
all_time = 0
count = 0

print(f"Введите количество примеров: {N}")
for i in range(N):
    count += 1
    print(f"вопрос {count}/{N}")
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    start_time = time.time()
    res = a * b
    try:
        user_res = int(input(f"{a} * {b} = "))
        time_spend = time.time() - start_time
        all_time += time_spend
        if user_res == res:
            print(f"верно! (Время: {time_spend:.2f})")
            correct += 1
        else:
            print(f"неверно! Правильно: {res} (Время: {time_spend:.2f})")
    except ValueError:
        print("Пожалуйста, введите целое число!")


average_time = all_time / N
average_correct = (correct / N) * 100

print("==================================================")
print("СТАТИСТИКА:")
print("==================================================")
print(f"среднее время {average_time:.2f}")
print(f"общее время {all_time:.2f}")
print(f"Правильных ответов: {correct}/{N} ")
print(f"процент правильных: {average_correct}%")
