def count_Text(x1, x2, x3):

    Max = 0
    count1 = 0
    count2 = 0
    count3 = 0
    while True:

        count = 0
        for i in range(len(x1)):

            count += 1

        if count > Max:
            Max = count

        count1 += count

        count = 0
        for i in range(len(x2)):

            count += 1

        if count > Max:
            Max = count

        count2 += count

        count = 0
        for i in range(len(x3)):
            count += 1

        if count > Max:
            Max = count

        count3 += count
        break

    if count1 + count2 == count1 + count3 and count2 + count3 == count1 + count2:
        print("All the same")

    elif count1 == count2 or count1 == count3 or count2 == count3:
        print("Neither")

    else:
        print(Max)

n1 = input().__str__()
n2 = input().__str__()
n3 = input().__str__()

count_Text(n1, n2, n3)