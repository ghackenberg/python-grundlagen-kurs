################
# Dictionaries #
################

# Literale

x = "a"
y = 1

a = {} # leeres Dictonary
b = { 1: "a" } # Dictionary mit einem Eintrag (Schlüssel = 1, Wert = "a")
c = { 1: "a", 5: "b" } # Dictionary mit zwei Einträgen
d = { "a": 1, "b": 5 } # Zeichenketten als Schlüssel und Zahlen als Werte
e = { "a": "x", "b": "y" } # Sowohl Schüssel als auch Werte sind Zeichenketten
f = { "a": [1, 2, 3], "b": ["a", "b", "c"] }
g = { "a": 1 + 5, "b": "str" + "str" }
h = { "a" + "b": 1 + 5 }
i = { "a": {} }
j = { "a": { 1: 1 }}
k = { int: "int", float: "float" }
l = { x + "a": y + 1 }

# Ergebnis der Schlüsselberechnung muss hashbarer Wert sein!
# Ergebnis der Wertberechnung kann beliebig sein.


# Operator []

# - Lesender Zugriff

print(b[1])
print(c[5])
print(k[int]) # -> "int"

# - Schreibender Zugriff

k[int] = "integer"

print(k[int]) # -> "integer"

# Operator in / not in

print(1 in b) # -> True
print(int in k) # -> True