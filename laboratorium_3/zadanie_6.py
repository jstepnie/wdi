import sys

a = float(input("podaj pierwszą liczbę:"))
b = float(input("podaj drugą liczbę:"))
if a < 0 and b < 0:
    print("obie liczby są mniejsze od zera, koniec programu")
    sys.exit(0)
if a < 0:
    fabs_a = -a
else:
    fabs_a = a
if b < 0:
    fabs_b = -b
else:
    fabs_b = b

print("suma:", fabs_a + fabs_b,\
      "różnica", fabs_a - fabs_b)
print("iloczyn", fabs_a * fabs_b\
    ,"iloraz", fabs_a / fabs_b)
if fabs_a * fabs_b == 10:
    print("Yay!")

print("potęga pierwszej liczby", fabs_a ** 2)
print("potęga drugiej liczby", fabs_b ** 2)
element_1 = fabs_a ** (1.0 / 2)
element_2 = fabs_b ** (1.0 / 2)
print("pierwiastek pierwszej:", element_1)
print("pierwiastek drugiej:", element_2)

# zrobiona pierwsza część



