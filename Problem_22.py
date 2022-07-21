I = int(input())
lst = []

count = 0
while count != I:
    n = input().__str__()
    count += 1
    lst.append(n)

def powernumber(x1,x2):

    count = 0
    for i in range(len(x2)):

        print(int(x2[i]) ** int(x2[i]))
        count += 1

        if count == x1:
            break

powernumber(I,lst)