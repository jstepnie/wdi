
number = int(input("Podajliczbę naturalną: "))
x = 1
number_2 = number // 2
list = []
while True:
    if number <= 0:
        print("liczba ma być naturalna i nie być zerem")
        break
    else:
        for i in range(1, number_2 + 1):
            if number % i == 0:
                print("fajnie",i)
                x = i
                list = list + [x]
                print(list)
                y = number / x
                if abs(x - y) < number - 1:
                    multiplication = x * y
                    print(y, "*", x)
                elif abs(x - y) <
                else:
                    multiplication = number * 1
                    print("rozkład na iloczyn o najmniejszej różnicy to: ", number, "*", 1)

            else:
                x = x
                list = list
                y = number / x


        break



