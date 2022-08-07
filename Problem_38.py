lab = 5
midterm = 20
final = 25

i_lab = int(input())
i_midterm = int(input())
i_final = int(input())

if (i_lab, i_midterm, i_final) >= (lab, midterm, final):
    print("pass")

else:
    print("fail")