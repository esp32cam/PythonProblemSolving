def detected_num(x):
    count1 = 0
    count = 0
    for i in range(len(x)):

        count += 1
        if int(x[i]) == 1:
            count1 += 1

    if  count > 5:
        print("Too long")

    elif count < 3:
        print("Too short")

    elif count == 3 or count == 4 or count == 5:
        print(count1)

n = input().__str__()
detected_num(n)