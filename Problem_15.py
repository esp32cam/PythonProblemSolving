def detected_text(x):
    count = 0
    count1 = 0
    for i in range(len(x)):

        if x[i].isupper() == True:
            count += 1

        elif x[i].islower() == True:
            count1 += 1

    if count1 == 4:
        print("Small Letter")

    elif count == 4:
        print("Capital Letter")

    else:
        print("Mix")

n = input().__str__()
detected_text(n)