
filepathA = "plik.txt"
filepathB = "plikB.txt"
filepathC = "plikC.txt"
def pobranie_danych(filepath):
    f = open(filepath, "r", encoding="utf-8")
    words = f.readlines()
    print(words)
    return words

def repetition(wordsA, wordsB):
    repeat = []
    for element in wordsA:
        if wordsB.count(element) != 0:
            repeat.append(element)
    print(repeat)
    return repeat

def addition(wordsA, wordsB, repetition, filepathC):
    wordsA1 = wordsA[:]
    wordsB1 = wordsB[:]
    repetition1 = repetition[:]
    for element in repetition:
        if wordsA.count(element) != 0:
            wordsA1.pop(wordsA1.index(element))
        if wordsB.count(element) != 0:
            wordsB1.pop(wordsB1.index(element))
    wordsA1 = str(wordsA1).replace("[", "").replace("]", "").replace(",", " ").replace("'", "")
    wordsB1 = str(wordsB1).replace("[", "").replace("]", "").replace(",", " ").replace("'", "")
    repetition1 = str(repetition1).replace("[", "").replace("]", "").replace(",", " ").replace("'", "")
    plikC = open(filepathC, "a")
    plikC.write(wordsA1)
    plikC.write("\n")
    plikC.write(wordsB1)
    plikC.write("\n")
    plikC.write(repetition1)
    plikC.close()

def substraction(wordsA, repetition, filepathC):
    wordsA1 = wordsA[:]
    repetition1 = repetition[:]
    for element in repetition:
        if wordsA.count(element) != 0:
            wordsA1.pop(wordsA1.index(element))
    wordsA1 = str(wordsA1).replace("[", "").replace("]", "").replace(",", " ").replace("'", "")
    plikC = open(filepathC, "a")
    plikC.write(wordsA1)
    plikC.close()

def multiplication(repetition, filepathC):
    repetition1 = repetition[:]
    for element in repetition1:
        plikC = open(filepathC, "a")
        repetition2 = str(element).replace("[", "").replace("]", "").replace(",", " ").replace("'", "")
        plikC.write(repetition2)
        plikC.close()

pobranieA = pobranie_danych(filepathA)
pobranieB = pobranie_danych(filepathB)
repetitionU = repetition(pobranieA, pobranieB)
# addition(pobranieA, pobranieB, repetitionU, filepathC)
# substraction(pobranieA, repetitionU, filepathC)
# multiplication(repetitionU, filepathC)