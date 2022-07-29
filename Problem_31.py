I = int(input())
i = 0
lst = []
while i != I*2:
    n = int(input())
    lst.append(n)
    i += 1

lst2 = []
count_i = 0
while count_i == 0 or count_i == 1:
    count_i = 0

    for i in range(len(lst)):

        if len(lst) - 1 != i:

            if lst[0] < lst[1]:
                lst2.append(lst[1])
                lst.pop(lst[0])
                lst.append(0)
                lst.pop(lst[0])
                count_i += 1

            elif lst[0] > lst[1]:
                lst2.append(lst[0])
                lst.pop(lst[0])
                lst.append(0)
                lst.pop(lst[0])
                count_i += 1

summ = 0
for i in range(len(lst2)):

    if len(lst2) - 1 != i:

        summ += lst[i]

print(summ)

n = int(input())

i = 0
lst = []

while i != n:
    a = int(input())
    b = int(input())
    if a > b:
        lst.append(a)
    if a < b:
        lst.append(b)
    i += 1

str1 = ""
str2 = " + "
cal = sum(lst)

for i in range(len(lst)):

    if i != len(lst) - 1:

        str1 += str(lst[i])
        str1 += str2

    else:
        str1 += str(lst[i])
        str1 += " = "
        str1 += str(cal)

print(str1)