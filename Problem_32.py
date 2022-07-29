n1 = int(input())
n2 = int(input())
i = n1
lst = []
str1 = ""
while i != n2+1:
    lst.append(i)
    str1 += str(i)
    str1 += " "
    i += 1

lst2 = []
for i in range(len(lst)):

    if lst[i] % 2 != 0:

        lst2.append(lst[i])

print(str1)
print(sum(lst2))