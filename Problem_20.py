str1 = (input()).lower()
result = ""
for i in range(len(str1)-1, -1, -1):
    result += str1[i]
print(result)