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
    chars = "XZZYXXXYYYXZZYYYY"

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


with open("46982.txt") as file:
    chars = file.read()


count = 0
idx = 0

while idx < len(chars):
    if chars[idx] == "E":
        end = idx + 1
        while end < len(chars) and chars[end] not in "EF":
            end += 1
        if end < len(chars) and end - idx + 1 >= 12 and chars[end] == "E":
            count += 1
            idx = end
        else:
            idx += 1
    else:
        idx += 1

print("#3")
print(f"Groups: {count}")


