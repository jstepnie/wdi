print("Program rozkładający liczbę naturalną na iloczyn dwóch liczb takich, że różnica między nimi jest najmniejsza")
while True:
    try:
        number = float(input("Podaj liczbę naturalną: "))
        if number == 0:
            raise ValueError(print("nie może być zero"))
        if number <= 1:
           raise  ValueError("liczba ma być naturalna i nie być zerem, ani jedynką")
        elif number % 1 != 0:
            raise ValueError("liczba musi być naturalna!")
        x = 1
        number_2 = number // 2
        list_m = []  #lista podzielników
        list_sub = []  #lista różnic
        while True:
                number = int(number)
                number_2 = int(number_2)
                for i in range(1, number_2 + 1):

                    if (number % i == 0) and list_m.count(i) == 0:
                        print("dzielnik liczby to: ", i)
                        x = i
                        list_m = list_m + [x]
                        y = number // x
                        list_m = list_m + [y]
                        list_sub = list_sub + [abs(x - y)]
                    else:
                        x = x
                        list_m = list_m
                        y = number // x
                print(list_m)
                # print(list_sub)
                for d in list_m:
                    if min(list_sub) == (d - (number / d)):
                        print("iloczyn, o najmniejszej różnicy składników, tworzący tą liczbę: ")
                        print(number, "=", d, "*", (number / d))
                        # print("zaczynamy na nowo:")
                    else:
                        list_m = list_m
                break
        break
    except ValueError:
        print("nie podano liczby naturalnej")


#przykłady testowe - 2342938472 = 41838187.0 * 56, -5 - nie zwróci,



