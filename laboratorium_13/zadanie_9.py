
while True:
    try:
        liczba = float(input("podaj liczbę naturalną dodatnią: "))
        if liczba < 0 or liczba % 1 != 0:
            raise ValueError
        print(liczba)

        def rozkladnasume(liczba, i):
            listasum = []
            if liczba == 1:
                print('koniec')
                return 1
            else:
                # for i in range(int(liczba)):
                #     latawiec = str( i + rozkladnasume(liczba - i))
                #     listasum.append(latawiec)
                txt = "{} + {}".format(i, rozkladnasume(liczba - i, i))
                print(txt)
                return i + rozkladnasume(liczba - i)

        for i in range(int(liczba)):
            rozkladnasume(liczba,i)

    except ValueError:
        print("proszę podać liczbę naturalną dodatnią")