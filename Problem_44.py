n = int(input())

i = 0
str1 = ""
while i != n:
    str1 += "*"
    i += 1

for i in range(len(str1)):
    if i != len(str1) - 1:
        print(str1)