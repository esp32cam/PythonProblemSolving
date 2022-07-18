def hahaha(x):
    count_5 = 0
    for i in range(len(x)):
        if x[i] == "5":
            count_5 += 1
    if "555" not in x:
        print("none")
    elif "555" in x and count_5 == 3:
        print("hahaha")
    elif count_5 != 3:
        print("none")

n = input().__str__()
hahaha(n)