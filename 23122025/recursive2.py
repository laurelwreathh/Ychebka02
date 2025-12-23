def task1(start, target, must_be, flag=False):
    if start == must_be:
        flag = True

    if start > target:
        return 0

    if start == target:
        return 1 if flag else 0

    total = 0

    total += task1(start + 1, target, must_be, flag)
    total += task1(start + 2, target, must_be, flag)
    total += task1(start * 2, target, must_be, flag)

    return total

print("Task 1")
print(task1(3, 12, 10))
print(task1(7, 18, 16))


def task2(start, target, not_contains, flag=False):
    if start == not_contains:
        flag = True

    if flag or start > target:
        return 0

    if start == target:
        return 1

    total = 0

    total += task2(start+1, target, not_contains, flag)
    total += task2(start*2 + 1, target, not_contains, flag)

    return total

print()
print("Task 2")
print(task2(1, 27, 26))
print(task2(1, 14, 6))


def task3(start, target, contains ,not_contains, flag_contains=False, flag_not_contains=False):
    if start == contains:
        flag_contains = True

    if start == not_contains:
        flag_not_contains = True


    if flag_not_contains or start > target:
        return 0

    if start == target :
        return 1 if flag_contains else 0

    total = 0

    total += task3(start + 1, target,contains,not_contains, flag_contains, flag_not_contains)
    total += task3(start + 2, target, contains,not_contains, flag_contains, flag_not_contains)

    return total

print()
print("Task 3")
print(task3(2, 18, 9, 14))
