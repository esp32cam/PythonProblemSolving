lst = ["a", "e", "i", "o", "u"]

n = input().__str__()
count = 0
for i in range(len(n)):

    if n[i] in lst:
        count += 1

print(count)


