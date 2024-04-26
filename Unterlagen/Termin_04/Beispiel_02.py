# Globale Variable

c = 5

# Funktion mit Parametern (= lokale Variablen)

def summeBerechnen(a, b):
    if type(a) is int:
        return a + b + c
    else:
        print("X")
        return a
        # raise Exception("Datentyp nicht unterstützt!")

# Funktionsaufrufe mit unterschiedlichen Werten für die Parameter

d = summeBerechnen(1, 2)
e = summeBerechnen("a", "b")
f = summeBerechnen("a", 1)