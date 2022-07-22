even = []
odd = []
while True:
    i = input()
    countodd = 0
    counteven = 0

    if i == "-1":
        for i in range(len(odd)):
            countodd += 1
        for i in range(len(even)):
            counteven += 1
        print(countodd)
        print(counteven)

        break
    elif int(i) % 2 == 0:
        even.append(i)
    elif int(i) % 2 != 0 and int(i) > 0:
        odd.append(i)