

a = int(input("Podaj wysokość choinki:"))

for pac in range(0, a):

    for verse in range(0, a - (pac + 1)):
        print(end = " ")
    if pac == 0:
        print("x", end = "")

    else:
        for verse in range(0,2 * (pac + 1) - 1):
            if pac == 3:
                print("0", end = '')
            else:

                print('*', end = "")
    print('\r')
print((a) * " ","U")
