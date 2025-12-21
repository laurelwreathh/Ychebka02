#1

import csv

with open("36031.csv", "r") as file:
    table = list(csv.reader(file))
    for i in range(len(table)):
        table[i] = list(map(int, table[i][0].split(';')))

reversed_table = [row[::-1] for row in table[::-1]]

for i in range(len(reversed_table)):
    for j in range(len(reversed_table[i])):
        if i == 0 and j == 0:
            reversed_table[i][j] = [reversed_table[i][j], ["старт"]]
        elif i == 0:
            value = reversed_table[i][j] + reversed_table[i][j - 1][0]
            path = reversed_table[i][j - 1][1] + ["влево"]
            reversed_table[i][j] = [value, path]
        elif j == 0:
            value = reversed_table[i][j] + reversed_table[i - 1][j][0]
            path = reversed_table[i - 1][j][1] + ["вверх"]
            reversed_table[i][j] = [value, path]
        else:
            if reversed_table[i - 1][j][0] >= reversed_table[i][j - 1][0]:
                value = reversed_table[i][j] + reversed_table[i - 1][j][0]
                path = reversed_table[i - 1][j][1] + ["вверх"]
                reversed_table[i][j] = [value, path]
            else:
                value = reversed_table[i][j] + reversed_table[i][j - 1][0]
                path = reversed_table[i][j - 1][1] + ["влево"]
                reversed_table[i][j] = [value, path]

result = reversed_table[-1][-1]
print(result[0],";",  result[1])


#2

import csv

with open("59778.csv", "r") as file:
    rows = list(csv.reader(file))

numbers = []
for i in range(len(rows)):
    row = rows[i][0].split(";")
    row = [int(x) for x in row]
    numbers.append(row)

count_rows = 0

for i in range(len(numbers)):
    found = False
    for j in range(len(numbers[i])):
        if numbers[i].count(numbers[i][j]) == 4 and not found:
            repeated_number = numbers[i][j]
            other_numbers = []

            for value in numbers[i]:
                if value != repeated_number:
                    other_numbers.append(value)

            other_numbers = list(set(other_numbers))

            if len(other_numbers) > 0:
                sum_repeated = 4 * repeated_number
                average_other = sum(other_numbers) / len(other_numbers)

                if average_other > sum_repeated:
                    count_rows += 1
                    found = True

print(count_rows)


#3

import csv

numbers = []

with open("29666.csv", 'r') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        numbers.extend([float(x.replace(',', '.')) for x in row])

max_sum = numbers[0]
length = len(numbers)

for i in range(length):
    current_sum = numbers[i]
    local_max = numbers[i]

    for j in range(i + 1, length):
        if numbers[j] < numbers[j - 1]:
            current_sum += numbers[j]
            if current_sum > local_max:
                local_max = current_sum
        else:
            break

    if local_max > max_sum:
        max_sum = local_max

print(max_sum)

