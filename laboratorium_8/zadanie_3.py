import random
print("program losujący n liczb nieparzystych z zakresu 1-99 i wyznaczający różnicę między ilością elementów w najdłuższych ciągach o r < 0 i r > 0")
while True:
    try:
        liczba = float(input("podaj liczbę naturalną dodatnią: "))
        if liczba <= 0 or liczba % 1 != 0:
            raise ValueError
        print(liczba)

        def rFinder(tab : list): #funkcja sprawdzająca czy kolejne elementy tworzą ciąg arytmetyczny
            nlength = 0
            plength = 0
            # rC1 = 0
            # rC2 = 0
            ntab = []
            ptab = []
            for i in range(len(tab)-2):
                r0 = tab[i+1] - tab[i]
                r1 = tab[i+2] - tab[i+1]
                # print(r0, r1)
                if r0 == r1:
                    print(r0)
                    if r0 < 0:
                        if nlength > 0:
                            nlength += 1
                        else:
                            nlength += 3
                    elif r0 > 0:
                        if  plength > 0:
                            plength += 1
                        else:
                            plength += 3
                else:
                    ntab.append(nlength)
                    ptab.append(plength)
                    nlength = 0
                    plength = 0
            ntab.append(nlength)
            ptab.append(plength)



            print("Najdłuższy ciąg o ujemnej różnicy ma {} cyfr".format(max(ntab)))

            print("Najdłuższy ciąg o dodatniej różnicy ma {} cyfr".format(max(ptab)))
            print("Różnica między ilością elementów w tych ciągach(d - u) {}".format(max(ptab) - max(ntab)))

        def listGenerator(N : int): #utworzenie listy N nieparzystych liczb pseudolosowych(

            tab = []

            while len(tab) <= N:
                i = random.randint(1, 99)
                if i % 2 != 0:
                    tab.append(i)
            return tab

        rFinder(listGenerator(liczba))
        rFinder([1,2,3,4,7,3,2,1])
        break
    except ValueError:
        print("proszę podać liczbę naturalną dodatnią")