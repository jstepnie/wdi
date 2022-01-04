
filepathA = "plik.txt"
filepathB = "plikB.txt"
filepathC = "plikC.txt"
def pobranie_danych(filepath):
    f = open(filepath, "r", encoding="utf-8")
    words = f.read().splitlines()
    elements = []
    for element in words:
        element1 = element.split()
        elements.append(element1)
    print(elements)
    return elements

def repetition(wordsA, wordsB):
    repeat = []
    for y1 in wordsA:
        for x1 in y1:
            for y2 in wordsB:
                if y2.count(x1) != 0 and repeat.count(x1) == 0:
                    repeat.append(x1)
    print(repeat)
    return repeat

def addition(wordsA, wordsB, repetition, filepathC):
    wordsA1 = []
    wordsB1 = []
    repetition1 = repetition[:]
    for y1 in wordsA:
        for x1 in y1:
            wordsA1.append(x1)
    for y2 in wordsB:
        for x2 in y2:
            wordsB1.append(x2)
    for element in repetition1:
        if wordsA1.count(element) != 0:
            wordsA1.remove(element)
        if wordsB1.count(element) != 0:
            wordsB1.remove(element)
    plikC = open(filepathC, "a")
    n = 0
    a = 0
    b = 7
    for elementa in wordsA1:
            if n < 7:
                plikC.write(str(elementa))
                plikC.write(" ")
                n = n + 1
            if n == 7:
                n = 0
                plikC.write("\n")
                plikC.write(str(wordsB1[a:b]).replace("[", "").replace("]", "").replace(",", " ").replace("'", ""))
                plikC.write("\n")
                a = a + 7
                b = b + 7
    plikC.write("\n")
    for element in repetition1:
        plikC.write(str(element))
        plikC.write(" ")
    plikC.close()

def substraction(wordsA, repetition, filepathC):
    wordsA1 = []
    n = 0
    for y1 in wordsA:
        for x1 in y1:
            wordsA1.append(x1)
    repetition = repetition[:]
    for element in repetition:
        if wordsA1.count(element) != 0:
            wordsA1.pop(wordsA1.index(element))
    plikC = open(filepathC, "a")
    for elementa in wordsA1:
            if n < 7:
                plikC.write(str(elementa))
                plikC.write(" ")
                n = n + 1
            if n == 7:
                n = 0
                plikC.write("\n")
    plikC.close()

def multiplication(repetition, filepathC):
    repetition1 = repetition[:]
    repetition1.sort()
    for element in repetition1:
        plikC = open(filepathC, "a")
        for i in range(7):
            repetition2 = str(element).replace("[", "").replace("]", "").replace(",", " ").replace("'", "")
            plikC.write(repetition2)
            plikC.write(" ")
        plikC.write("\n")
        plikC.close()

pobranieA = pobranie_danych(filepathA)
pobranieB = pobranie_danych(filepathB)
repetitionU = repetition(pobranieA, pobranieB)
# addition(pobranieA, pobranieB, repetitionU, filepathC)
# substraction(pobranieA, repetitionU, filepathC)
multiplication(repetitionU, filepathC)
