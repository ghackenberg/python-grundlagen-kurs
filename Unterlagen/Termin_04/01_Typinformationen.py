# Funktionen mit Parametern (lokalen Variablen)

def f2(a, b):
    # Globale Variablen a und b werden durch Parameter verdeckt!
    return a * b

def f(a):
    # Globale Variable a wird durch Parameter verdeckt!
    # Globale Variable b wird nicht verdeckt!
    return f2(a + 1, b + 1) + b

# Globale Variablen

a = 5
b = 5
c = a + b

# Funktionsaufruf mit lokalen Variablen, die globale Variablen überdecken

d = f(1)

# Funktionen sind auch Variablen (mit Datentyp Funktion)

x = type(type(f))

print(x)

# Sonstiges zu Datentypen und Datentypliteralen

type(1) is int
type(1.1) is float

type(function) is type
type(int) is type
type(float) is type
type(str) is type
type(list) is type
type(dict) is type