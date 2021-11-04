import random
task = ""
while True:
    number_1 = int(input("Podaj liczbę 1: "))
    number_2 = int(input("Podaj liczbę 2: "))
    print("""
    Wybierz rodzaj działania:
    "+" - dodawanie
    "-" - odejmowanie
    "*" - mnożenie
    "/" - dzielenie
    "**" - potęgowanie
    "#" - pierwiastkowanie 
    "L" - losowanie liczby(podaj całkowite)
    """)
    task = input("Wybierz rodzaj działania: ")
    if task == "+":
        sum = number_1 + number_2
        print("suma to: ", sum)
        response = input("czy chcesz zrobić inne obliczenia? (T/N)")
        if response != "T":
            print("koniec zabawy")
            break
        else:
            print("zabawa od nowa")
    elif task == "-":
        subs = number_1 - number_2
        print("różnica to: ", subs)
        response = input("czy chcesz zrobić inne obliczenia? (T/N)")
        if response != "T":
            print("koniec zabawy")
            break
        else:
            print("zabawa od nowa")
    elif task == "*":
        mult = number_1 * number_2
        print("iloczyn to: ", mult)
        response = input("czy chcesz zrobić inne obliczenia? (T/N)")
        if response != "T":
            print("koniec zabawy")
            break
        else:
            print("zabawa od nowa")
    elif task == "/":
        if number_2 == 0:
            print("nie wolno tak")
            break
        else:
            div = number_1 / number_2
            print("wynik dzielenia: ", div)
            response = input("czy chcesz zrobić inne obliczenia? (T/N)")
            if response != "T":
                print("koniec zabawy")
                break
            else:
                print("zabawa od nowa")
    elif task == "**":
        power = number_1 ** number_2
        print("potęga liczby to: ", power)
        response = input("czy chcesz zrobić inne obliczenia? (T/N)")
        if response != "T":
            print("koniec zabawy")
            break
        else:
            print("zabawa od nowa")
    elif task == "#":
        if number_1 < 0:
            print("ma być dodatnia")
            break
        else:
            element = number_1 ** (1 / number_2)
            print("pierwiastek wynosi: ", element)
            response = input("czy chcesz zrobić inne obliczenia? (T/N)")
            if response != "T":
                print("koniec zabawy")
                break
            else:
                print("zabawa od nowa")
    elif task == "L":
        if number_1 >= number_2:
            field = random.randint(number_1, number_2)
            print("wylosowana liczba to: ", field)
            response = input("czy chcesz zrobić inne obliczenia? (T/N)")
            if response != "T":
                print("koniec zabawy")
                break
            else:
                print("zabawa od nowa")
        else:
            field = random.randint(number_2, number_1)
            print("wylosowana liczba to: ", field)
            response = input("czy chcesz zrobić inne obliczenia? (T/N)")
            if response != "T":
                print("koniec zabawy")
                break
            else:
                print("zabawa od nowa")
