# Vorschau: Rekursive Funktionen (Funktionen, die sich selber aufrufen)

# Beispiel 1: Implementierung der Exponentialfunktion als rekursive Funktion

def Exponentialfunktion(x, n):
    if n == 0:
        return 1
    else:
        return x * Exponentialfunktion(x, n - 1)

Exponentialfunktion(3, 4)

# Beispiel 2: Implementierung der Fakultätsfunktion als rekursive Funktion

def Fakultätsfunktion(n):
    if n == 0:
        return 1
    else:
        return n * Fakultätsfunktion(n - 1)


Fakultätsfunktion(5)