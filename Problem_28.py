n = int(input())
i = 1
lst = []

while i != n+1:
    lst.append(i)
    i += 1

for i in range(len(lst)):

    if lst[i] % 5 != 0:
        print("*", end='')
    elif lst[i] % 5 == 0:
        print("X", end='')