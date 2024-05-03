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

# lesender Zugriff

print(b[0]) # -> 1
print(b[0:3]) # -> [1, 2, 3]
print((d[2])[0]) # -> a

print(type(b[0])) # -> int
print(type(b[0:1])) # -> list

# schreibenden Zugriff

a[0] = 6
b[1] = 7

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

len([1, 7, 9]) # -> 3
len("sdfh") # -> 4

# - Sortieren von Listen

[1, -1, 5, -6].sort() # -> [-6, -1, 1, 5]

# - Suche von Listenelementen

[1, 4, 5, 8, 10].index(4) # -> 1