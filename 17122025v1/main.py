print("Задача 1: Ход шахматного коня")
x1 = int(input("x первой клетки (1-8): "))
y1 = int(input("y первой клетки (1-8): "))
x2 = int(input("x второй клетки (1-8): "))
y2 = int(input("y второй клетки (1-8): "))

if not (1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8):
    print("Ошибка")
else:
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
        print("Да")
    else:
        print("Нет")

print()

print("Задача 2: Сумма четных чисел от K до N")
K = int(input("Введите число K: "))
N = int(input("Введите число N: "))

sum_even = 0
for i in range(K, N + 1):
    if i % 2 == 0:
        sum_even += i

print(f"Сумма четных чисел от {K} до {N} включительно: {sum_even}")
print()

print("Задача 3: Сумма чисел до ввода 0")
total_sum = 0
while True:
    num = int(input("Введите число (0 для завершения): "))
    if num == 0:
        break
    total_sum += num

print(f"Сумма введенных чисел: {total_sum}")
print()

print("Задача 4: Факториал числа N")
N = int(input("Введите число N: "))

factorial = 1
for i in range(1, N + 1):
    factorial *= i

print(f"Факториал числа {N} равен {factorial}")
