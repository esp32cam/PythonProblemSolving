i = int(input())

ten = int(i/10)
if ten > 0:
    print(ten)
else:
    print("0")

cal = ten * 10
i -= cal

five = int(i/5)
if five > 0:
    print(five)
else:
    print("0")

cal = five * 5
i -= cal

two = int(i/2)
if two > 0:
    print(two)
else:
    print("0")

cal = two * 2
i -= cal

one = i
if one > 0:
    print(one)
else:
    print("0")