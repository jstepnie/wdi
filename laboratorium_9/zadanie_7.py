print("Program tworzący tablicę n x n i dający True jeśli w każdym wierszu i kolumnie jest co najmniej jedno 0")
import random
while True:
    try:
        n = float(input("podaj wymiar n tablicy kwadratowej"))
        liczba = 3
        # liczba = float(input("podaj najwyższą liczbę, do której program losuje elementy do tablicy"))
        flag = 0
        testowa1 = [[0,1,2,3,4],[1,0,2,3],[1,2,0,3],[1,2,3,0]] #powino pokazać true
        testowa2 = [[1,2,0,4],[1,0,2,3],[0,2,3,4],[0,1,2,3]] #nie powinno zadziałać bo nie ma 0 w 4 kolumnie
        if n % 1 != 0 or n <= 0:
            raise ValueError
        wiersz = []
        n = int(n)
        tablica = [[random.randint(0,liczba) for x in range(n)] for y in range(n)]
        print(tablica)
        def zerofinder(tablica, n):
            miejsce = []
            flag = True
            for y in tablica:
                if y.count(0) == 0:
                    flag = False
                else:
                    while y.count(0) != 0:
                            miejsce.append(y.index(0))
                            y.remove(0)
            for i in range(0, n ):
                if miejsce.count(i) == 0:
                    flag = False
            print(flag)


        zerofinder(tablica, n)
        zerofinder(testowa1, 4)
        zerofinder(testowa2, 4)
        break

    except ValueError:
        print("to ma być liczba naturalna dodatnia")
