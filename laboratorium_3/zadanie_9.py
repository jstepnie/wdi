print("Dzień dobry, tutaj bankomato-wpłatomat")
a = int(input("ustaw pin:"))
b = int(input("potwierdź pin:"))
status = 0
while True:
    while True:
        if b != a:
            print("nieprawidłowo")
            break
        else:
            print("zatwierdzanie")
            break


    print("""Co chciałbyś zrobić?
    :deposit - wpłacenie
    :withdraw - wypłacenie
    :saldo - stan konta
    """ )
    demand = input()
    if demand == "deposit":
        deposit = int(input("ile pieniędzy wpłacasz?"))

        b = int(input("potwierdź pin:"))
        while True:
            if b != a:
                print("nieprawidłowo")
                break
            else:
                print("zatwierdzanie")
                break
        status += deposit
        print(status)
    elif demand == "withdraw":
        withdraw = int(input("Jaką kwotę chcesz wypłacić?"))
        b = int(input("potwierdź pin:"))
        while True:
            if b != a:
                print("nieprawidłowo")
                break
            else:
                print("zatwierdzanie")
                break
        while True:
            if withdraw > status:
                print("nie masz tyle na koncie")
                break
            else:
                print("wypłacono:", withdraw)
                status -= withdraw
                print("masz na koncie:", status)
                break
    elif demand == "saldo":
        b = int(input("potwierdź pin:"))
        while True:
            if b != a:
                print("nieprawidłowo")
                break
            else:
                print("zatwierdzanie")
                break
        print("masz na koncie:", status)
    else:
        print("nie rozumiem:")


