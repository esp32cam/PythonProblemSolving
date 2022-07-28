s = int(input())
lst = []
while True:

    n = int(input())
    lst.append(n)
    if n == 0:
        break

count = 0
Max = 0
for i in range(len(lst)):

    if i != len(lst) - 1:
        if lst[i] == s:
            if lst[i] == lst[i+1]:
                count += 1
            if lst[i] != lst[i+1]:
                if count > Max:
                    Max = count
print(Max)