a = int(input("Podaj pierwszą liczbę całkowitą:"))
b = int(input("Podaj drugą liczbę całkowitą:"))

if a > b:
    d = a
    e = b
    scope = range(b, a)
elif a < b:
    d = b
    e = a
    scope = range(a, b)
else:
    print("podano te same liczby, koniec programu")

if (a - b > 20 or b - a > 20):
    c = (a + b) // 2
    print(c - 3 ,c - 2  , c - 1)
    scope_1 = range(c + 1, d)

    for I in range(3): print(scope_1[I])

elif a > b:
    for I in range(a - b):
        print(scope[I])


else:
    for I in range(b - a): print(scope[I])

