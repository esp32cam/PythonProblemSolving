n = int(input())

def powernumber2(x):

    lst = []
    i = 0
    while i != x:
        i += 1
        lst.append(i)

    summ = 0
    for i in range(len(lst)):

        lst[i] **= 2
        summ += lst[i]

    print(summ)

powernumber2(n)