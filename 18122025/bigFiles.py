def task1(userFile):
    numbers = []

    with open(userFile, "r") as file:
        numbers = file.readlines()
        numbers = [int(elem) for elem in numbers]

    counter = 0
    max_sum = -10000000

    for i in range(len(numbers) - 1):
        a, b = numbers[i], numbers[i + 1]

        if ((a * b) % 15 == 0) and ((a + b) % 7 == 0):
            counter += 1
            max_sum = max((a + b), max_sum)

    return f"Пар: {counter}; Сумма: {max_sum}"


print(task1("39762.txt"))


def task2(userFile):
    # quads = 0
    # summa = 0
    # max_summa = 0
    #
    # with open(userFile, "r") as file:
    #     numbers = file.readlines()
    #     numbers = [int(elem) for elem in numbers]
    #
    # for i in range(len(numbers) - 3):
    #
    #     quad = numbers[i:i + 4]
    #
    #     if (sum(1 for x in quad if len(str(x)) == 5)) >= 1 and sum(1 for x in quad if x < 10000 or x > 99999) >= 2:
    #         if sum(1 for x in quad if x % 3 == 0) < sum(1 for x in quad if x % 7 == 0):
    #             max_elem = 0
    #             double_elem = 0
    #             for elem in quad:
    #                 if str(elem)[-3:] == "562":
    #                     if max_elem < elem:
    #                         max_elem = elem
    #                         double_elem = max_elem * 2
    #             for i in quad:
    #                 summa += i
    #             if max_summa < summa:
    #                 max_summa = summa
    #             if (summa > max_elem) and (double_elem > summa):
    #                 quads += 1
    # return f"Четвёрки {quads}; Сумма {max_summa}"

    with open(userFile, 'r') as file:
        chisla = file.readlines()
        chisla = [int(el) for el in chisla]
        max_el = 0
        for el in chisla:
            if str(el)[-3:] == "562":
                if max_el < el:
                    max_el = el
        c = 0
        max_sum = 0
        for i in range(len(chisla) - 3):
            l = [chisla[i], chisla[i + 1], chisla[i + 2], chisla[i + 3]]
            l5 = [el for el in l if len(str(el)) == 5]
            lnot5 = [el for el in l if len(str(el)) != 5]
            lcrat3 = [el for el in l if el % 3 == 0]
            lcrat7 = [el for el in l if el % 7 == 0]
            if len(l5) >= 1 and len(lnot5) >= 2:
                if len(lcrat3) < len(lcrat7):
                    if sum(l) > max_el and sum(l) < max_el * 2:
                        c += 1
                        if max_sum < sum(l):
                            max_sum = sum(l)
    print(c, max_sum)


task2("68279.txt")


def task3(userFile):
    with open(userFile, "r") as file:
        numbers = file.readlines()
        numbers = [int(f) for f in numbers]
    counter = 0
    count_odd = 0
    summ_odd = 0
    max_sum = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 == 1:
            count_odd += 1
            summ_odd += numbers[i]
    avg = summ_odd / count_odd
    for i in range(len(numbers) - 1):
        a, b = numbers[i], numbers[i + 1]
        if (a % 5 == 0 or b % 5 == 0) and (a < avg or b < avg):
            counter += 1
            if max_sum < (a + b):
                max_sum = (a + b)
    print(f"Счетчик {counter} Максимальная сумма {max_sum}")


task3("40992.txt")
