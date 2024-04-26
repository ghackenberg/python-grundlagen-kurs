##########
# Listen #
##########

# Literale

a = []
b = [1, 2, 3]
c = ["a", "b", "c"]
d = [[], [1, 2, 3], ["a", "b", "c"]]
e = [1, "1", [1, "2", [2]]]

# Operator []

print()
print("Operator []")
print()

print(b[0]) # -> 1
print(b[0:3]) # -> [1, 2, 3]
print(d[2][0]) # -> a

print(type(b[0])) # -> int
print(type(b[0:1])) # -> list

# Operator in / not it

print()
print("Operator in / not in")
print()

print(1 in b)
print(2 in b)
print(3 not in b)
print([] in d)
print([1, 2, 3] in d)

# Ausblick: Arbeiten mit Listen

# - Sortieren von Listen

[1, -1, 5, -6].sort()

# - Suche von Listenelementen

[1, 4, 5, 8, 10].index(4)