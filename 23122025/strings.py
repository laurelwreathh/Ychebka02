#1

with open("27686.txt", "r") as f:
    chars = f.read()

temp = 0
max_len = 0
for i in chars:
    if i != "X":
        temp = 0
    if temp > max_len:
        max_len = temp
    temp += 1

print("#1")
print(f"Max length: {max_len}")
print()



#2
with open("36037.txt", "r") as f:
    chars = f.read()

temp = 0
max_len = 0

for i in range(len(chars)):
    if chars[i:i+4] == "XZZY":
        temp = 0
        continue

    if temp > max_len:
        max_len = temp

    temp += 1

print("#2")
print(f"Max length: {max_len}")
print()


#3

with open("46982.txt", "r") as f:
    chars = f.read()

temp = 0
count_groups = 0
inside_group = False

for c in chars:
    if c == "F":
        if inside_group and temp >= 12:
            count_groups += 1
        temp = 0
        inside_group = False
        continue

    if c == "E":
        if not inside_group:
            temp = 1
            inside_group = True
        else:
            temp += 1
            if temp >= 12:
                count_groups += 1
            temp = 0
            inside_group = False
    else:
        if inside_group:
            temp += 1

print("#3")
print(f"Groups: {count_groups}")


