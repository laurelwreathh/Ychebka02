# 1
def fac(n):
    if n == 0:
        return 1
    return n * fac(n - 1)

print("\n#1")
print(fac(5))


# 2

def remove_vowels(s):
    vowels = ["a", "i", "e", "o", "u", "y"]

    if s == "":
        return ""

    if s[0] in vowels:
        return remove_vowels(s[1:])
    else:
        return s[0] + remove_vowels(s[1:])

print("\n#2")
print(remove_vowels("apple"))
print(remove_vowels("orange"))
print(remove_vowels("pear"))


# 3
def pascal(n):
    if n == 1:
        return [1]

    prev = pascal(n - 1)

    row = [1]

    for i in range(len(prev)-1):
        row.append(prev[i] + prev[i + 1])

    row.append(1)


    return row

print("\n#3")
print(pascal(1))
print(pascal(2))
print(pascal(3))
print(pascal(4))
print(pascal(5))
print(pascal(6))
print(pascal(7))
print(pascal(8))


#FINAL

def solve(maze, row = None, col = None):
    rows = len(maze)
    cols = len(maze[0])

    if row is None or col is None:
        for i in range(rows):
            for j in range(cols):
                if maze[i][j] == "s":
                    row, col = i, j

    if maze[row][col] == "x":
        return []

    maze[row] = maze[row][:col] + "#" + maze[row][col+1:]

    directions = [
        ('up', row - 1, col),
        ('down', row + 1, col),
        ('left', row, col - 1),
        ('right', row, col + 1)
    ]

    for move, r, c in directions:
        if 0 <= r < rows and 0 <= c < cols and maze[r][c] != "#":
            path = solve(maze, r, c)
            if path is not None:
                return [move] + path

    return None




mazeX = [
    's----',
    '##---',
    '---##',
    '----x'
]

mazeY = [
    '--x--',
    '##--#',
    '#--##',
    's-####'
]

print("\n#FINAL")
print(solve(mazeX))
print(solve(mazeY))