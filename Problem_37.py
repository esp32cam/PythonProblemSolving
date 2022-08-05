i1 = input().__str__()
i2 = input().__str__()
i3 = input().__str__()

if len(i1) > 5 and len(i2) > 5:
    var1 = i1[0] + i1[1] + i2[-1] + i3[-1]
    print(var1)

else:
    var = i1[0] + i3 + i2[-1]
    print(var)

