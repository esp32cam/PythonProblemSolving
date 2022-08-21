i1 = int(input())

lst = ["A", 'B', "C", "D", "E"]
i = 0
count = 0
while i != i1:
    while i != i1:
        print(lst[i] + " ", end='')
        i += 1
    print(" ")
    i = 0
    count += 1
    if count == 5:
        break