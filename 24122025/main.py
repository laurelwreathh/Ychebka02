# 1
for digit in range(15):
    total = int(f"123{digit}5", 15) + int(f"1{digit}233", 15)

    if total % 14 == 0:
        result_base10 = total // 14

        digits = "0123456789ABCDE"
        result_base15 = ""

        number = result_base10
        while number > 0:
            result_base15 = digits[number % 15] + result_base15
            number //= 15

        print(f"1: в 10 = {result_base10}, в 15 = {result_base15}")
        break

# 2
number1 = "AB267D1"
number2 = "F024A89"

digits = "0123456789ABCDEF"

sum_digits_1 = 0
for symbol in number1:
    for value in range(len(digits)):
        if digits[value] == symbol:
            sum_digits_1 += value
            break

sum_digits_2 = 0
for symbol in number2:
    for value in range(len(digits)):
        if digits[value] == symbol:
            sum_digits_2 += value
            break

total_digits_sum = sum_digits_1 + sum_digits_2

for base in range(16, total_digits_sum + 1):
    if total_digits_sum % (base - 1) == 0:
        number1_base10 = 0
        for symbol in number1:
            for value in range(len(digits)):
                if digits[value] == symbol:
                    number1_base10 = number1_base10 * base + value
                    break

        number2_base10 = 0
        for symbol in number2:
            for value in range(len(digits)):
                if digits[value] == symbol:
                    number2_base10 = number2_base10 * base + value
                    break

        numbers_sum = number1_base10 + number2_base10

        if numbers_sum % (base - 1) == 0:
            print(f"2: Система: {base}")
        break

# 3
for digit in range(10):
    number1 = digit * (17 ** 3) + 11 * (17 ** 2) + 9
    number2 = digit * (15 ** 3) + 8 * (15 ** 2) + 14 * 15 + 8

    total = number1 + number2

    if total % 155 == 0:
        print(f"3: x: {digit}, частное в 10: {total // 155}")
        break

# 4
symbols = '0123456789AB'
for x_value in range(8):
    for y_value in range(1, 8):
        x_symbol = symbols[x_value]
        y_symbol = symbols[y_value]

        number1 = int(y_symbol + '04' + x_symbol + '5', 11)
        number2 = int('253' + x_symbol + y_symbol, 8)

        total = number1 + number2

        if total % 117 == 0:
            print(f"4: отв = {total // 117}")

# 5
value = (7 * (512 ** 1912) + 6 * (64 ** 1954) - 5 * (8 ** 1991) - 4 * (8 ** 1980) - 2022)

eight = ""
while value > 0:
    eight += str(value % 8)
    value //= 8

count = 0
for digit in eight:
    if digit == "7":
        count += 1

print(f"5: количество 7: {count}")
