Max_odd = 0
Max_even = 0

while True:
    n = int(input())

    if n % 2 == 0 and n > Max_even:
        Max_even = n

    if n % 2 != 0 and n > Max_odd:
        Max_odd = n

    if n < 0:
        print(Max_odd)
        print(Max_even)
        print(abs(Max_even - Max_odd))
        break