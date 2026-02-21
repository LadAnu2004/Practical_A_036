n = 5
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()
rows = 5
for i in range(rows, 0, -1):
    for space in range(rows - i):
        print(" ", end="")
    for star in range(i):
        print("*", end=" ")
    print()
