def examining_num(x):

    for i in range(len(x)):

        if x[0] == x[-1] and x[0] == "9" or x[0] == "5":
            print("Very Luck")
            break

        elif x[0] == x[-1]:
            print("Lucky")
            break

        else:
            print("Usual")
            break

n = input().__str__()
examining_num(n)