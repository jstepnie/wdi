print("rozwiązanie metodą bisekcji równania x^2 - 2 = 0")
delta = 0.00001
element_1 = 1
element_2 = 20
tries = 100

def f(x):
    "dfinicja funkcji: "
    # print( (x ** 2) - 2)

    return (x ** 2) - 2

def bisection(tries, delta, function, element_1, element_2):
    for k in range(1, tries):
        mean = (element_1 + element_2) / 2

        if abs(function(mean)) < delta:
            return mean
        elif function(mean) * function(element_1) < 0:
            element_2 = mean
        else:
            element_1 = mean
    return None


m_zerowe = bisection(tries, delta, f, element_1, element_2)
print(m_zerowe)
print("drugie miejsce zerowe: ", - m_zerowe)
