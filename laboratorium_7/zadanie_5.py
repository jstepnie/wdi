import random

print("program losujący 1000 liczb między podanymi i znajdujący te składające się z cyfr nieparzystch")
while True:
    try:
        liczba_1 = float(input("Proszę podać liczbę, będącą dolną granicą zakresu: "))
        liczba_2 = float(input("Proszę podać drugą liczbę, większą od poprzedniej o ponad tysiąc: "))
        list_1 = []
        list_2 = []
        i = 0
        def reszta(wylosowana, kolejka):
            return wylosowana % kolejka

        if liczba_2 > liczba_1 + 1000:
            liczba_1 = liczba_1 // 1
            while i < 1000:
                a = random.randint(liczba_1, liczba_2)
                kolejka = 10
                cyfra = a % 10
                reszty = a % 10
                while cyfra % 2 != 0 and kolejka / 10 <= a: #szukanie liczb składających się z nieparzystych
                    cyfra = reszta(a - reszty, kolejka * 10)
                    reszty = reszty + cyfra
                    cyfra = cyfra / kolejka
                    # list_2 = list_2 + [cyfra]
                    kolejka = kolejka * 10
                    if a / (kolejka / 10) < 1:
                        print("Ta liczba składa się z samych cyfr nieparzystych: ", a)
                        break
                    else:
                        kolejka = kolejka

                if list_1.count(a) == 0: #dodwanie liczby do listy tak, żeby się nie powtarzały
                    list_1.append(a)
                    i = i + 1
                else:
                    list_1 = list_1

        elif liczba_1 == liczba_2:
            print("Mają być różne od siebie")
        else:
            print("Muszą być od siebie różne o ten tysiąc i jeden")
        list_1.sort() #sortowanie od najmniejszej i odwrócenie liczb w tablicy
        list_1.reverse()
        print(list_1)

    except ValueError:
        print("wprowadzono tekst nie liczbę")
        print("Janek to frajer pompka")

