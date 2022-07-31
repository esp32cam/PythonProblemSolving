cal = [0, 100, 120, 200, 60]
fruit = [0, "Apple", "Papaya", "Banana", "Orange"]

count_cal = 0
while True:
    a = int(input())

    for i in range(len(fruit)):

        if a == i:
            count_cal += cal[i]
            print("You choose %s" % fruit[i])

    if a == 5:
        print("Bye Bye")
        print("Total Calories:%d" % count_cal)