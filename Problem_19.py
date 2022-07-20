def fing_thehome(x):
    countX = 0
    countH = 0
    for i in range(len(x)):

        if x[i] == "X":
            countX += i

        if x[i] == "H":
            countH += i

    cal = countH - countX
    if cal > 0:
        print("R%d" % abs(cal))

    else:
        print("L%d" % abs(cal))

n = input().__str__()
fing_thehome(n)