n = input().__str__().split()

def powercount(x):

    i = int(x[0])
    lst = []

    while i <= int(x[1])+1 and i >= int(x[0]):
        lst.append(i)
        i += 1

    summ = 0
    for i in range(len(lst)):

        if int(lst[i]) % 2 != 0:
            print("%d " % i, end="")
            summ += i

    print("")
    print(summ)

powercount(n)

a, b = [int(e) for e in input().split()]
sum = 0
i = a
while i <= b:
    if i % 2 != 0:
        print("%d " % i, end='')
        sum += i
    i += 1
print('')
print(sum)