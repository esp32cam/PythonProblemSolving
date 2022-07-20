I = int(input())
count = 0
lst = []

while count != I:
    count += 1
    N = input().__str__()
    lst.append(N)


def looping(x, x1):
    count = 0
    min = 1000
    for i in range(len(x1)):

        count += 1
        if int(x1[i]) < min:
            min = int(x1[i])

        if count == x:
            break

    print(min)


looping(I, lst)