"""for i in range(0, 5):
    for j in range(0, i+1):
        print("*", end=" ")
    print()"""

m = 6
for i in range(0, 6):
    for j in range(0, m):
        print(end=" ")
    m -= 1
    for k in range(0, i):
        print("*", end=" ")
    print()

for i in range(6, 0, -1):
    for j in range(0, m):
        print(end=' ')
    m += 1
    for k in range(1, i + 1):
        print("*", end=" ")
    print()
