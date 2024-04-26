###################################
# Verzweigungsart 1: if-elif-else #
###################################

Bedingung1 = False # Ein boolscher Wert, kann Ergebnis einer Berechnung sein
Bedingung2 = True
Bedingung3 = True

# Einfache bedingte Ausführung

if Bedingung1:
    print("test")

# Bedingte Ausführung mit einem alternativen Zweig

if Bedingung1:
    print("a")
elif Bedingung2:
    print("b")

# Bedingte Ausführung mit einem universellen Ausweichzweig

if Bedingung1:
    print("a")
else:
    print("b")

# Mischung der obigen Varianten (und komplexe Bedingungen)

if Bedingung1 and type(Bedingung1) is bool:
    print("a")
elif Bedingung2:

    # Unterverzweigung, die unabhängig von der übergeordneten Verzweigung ist

    if Bedingung1 or Bedingung2:
        print("b")
    elif Bedingung3 or 5 > 2:
        print("c")
    else:
        print("d")

elif Bedingung3:
    print("e")
else:
    print("f")

# Abdeckung größerer Wertebereiche in einem Zweig

i = 5

if i > 0 and i < 10:
    print("x")

#################################
# Verzweigungsart 2: match-case #
#################################

Wert = 1, 2 # -> Tupel! Unveränderliche Liste

Wert[0]
Wert[1]

match Wert:
    case 1, 2:
        print("a")
    case 2:
        print("b")
    case 3:
        print("c")
    case _:
        print("d")

###############################################
# Verzweigungsart 3: try-raise-except-finally #
###############################################

# Grundlegender Aufbau eines try-raise-except-finally Blocks
# Ausführung des try Blocks wird abgebrochen, wenn eine Ausnahme ausgelöst wird
# Die Ausführung spring dann zum nächsten übergeordneten except Block
# Mehrere except Blöcke können anhand des Datentyps der Ausnahme unterschieden werden
# Der finally Block kann schließlich für Aufräumarbeiten verwendet werden (Dateien, Sockets, ...)

try:
    print("a")
    raise TypeError()
    print("b")
except IndexError:
    print("c")
except TypeError:
    print("d")
except int:
    print("e")
except str:
    print("f")
finally:
    print("g")

# Operatoren können auch Ausnahmen auslösen

try:
    "a" + 1
except:
    print("Fehler!")

try:
    [1, 2][5]
except:
    print("Fehler!")

# Funktionen lösen meistens auch Ausnahmen aus

def summe(a, b):
    if type(a) is int and type(b) is int:
        return a + b
    else:
        raise Exception("Fehler!")