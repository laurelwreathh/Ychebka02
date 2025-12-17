# # 1 fibonacci
#
# def fib(x):
#     l = [0, 1]
#     for i in range(x-2):
#         new = l[0] + l[1]
#         l = [l[1], new]
#     return l[1]
#
# x = int(input("Введите число число фибоначи"))
# print(fib(x))
#
# # 2. Задача о кузнечике
# def cuznecik(n):
#     l = [1,1,2]
#     for i in range(x-3):
#         new = l[0] + l[1] + l[2]
#         l = [l[1], l[2], new]
#     return l[2]
#
# n = int(input("Enter n: "))
# print(cuznecik(n))


#3. Задача о монетках



coins = [
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 40, 70, 0, 0, 1],
    [100, 0, 0, 0, 0, 1],
]

n = 4
m = 6

for i in range(n):
    for j in range(m):
        coins[i][j] = [coins[i][j], []]
        if i == 0 and j == 0:
            continue

        value = coins[i][j][0]

        if i == 0 and j != 0:
            coins[i][j][0] = coins[i][j][0] + coins[i][j - 1][0]
            coins[i][j][1] = coins[i][j - 1][1][:]
            coins[i][j][1].append("вправо")

        elif i != 0 and j == 0:
            coins[i][j][0] = coins[i][j][0] + coins[i - 1][j][0]
            coins[i][j][1] = coins[i - 1][j][1][:]
            coins[i][j][1].append("вниз")

        else:
            maxNum = max(coins[i - 1][j][0], coins[i][j - 1][0])

            if maxNum == coins[i - 1][j][0]:
                coins[i][j][0] = coins[i][j][0] + coins[i - 1][j][0]
                coins[i][j][1] = coins[i - 1][j][1][:]
                coins[i][j][1].append("вниз")
            else:
                coins[i][j][0] = coins[i][j][0] + coins[i][j - 1][0]
                coins[i][j][1] = coins[i][j - 1][1][:]
                coins[i][j][1].append("вправо")

print("Максимальная сумма:", coins[-1][-1][0])
print("Путь:", " -> ".join(coins[-1][-1][1]))