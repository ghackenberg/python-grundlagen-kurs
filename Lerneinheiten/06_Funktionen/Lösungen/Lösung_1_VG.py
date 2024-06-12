# Initialisierung des Spielfelds


spielfeld = []

for i in range(6):
    zeile = []
    for j in range(7):
        zeile.append(0)
    spielfeld.append(zeile)


# Hilfsfunktionen


def spielfeldAusgeben():
    for i in range(6):
        print(spielfeld[i])


def spielende():
    return False


def spalteFrei(spalte: int):
    return spielfeld[0][spalte] == 0


def spielfeldAktualisieren(spalte: int, spielernummer: int):
    for i in range(5, -1, -1):
        if spielfeld[i][spalte] == 0:
            spielfeld[i][spalte] = spielernummer
            return


# Spielschleife


spielfeldAusgeben()

while not spielende():

    # TODO Eingabe wiederholen, wenn Spalte voll
    spalte1 = int(input("Spieler 1"))
    if spalteFrei(spalte1):
        spielfeldAktualisieren(spalte1, 1)
        spielfeldAusgeben()

    # TODO Eingabe wiederholen, wenn Spalte voll
    spalte2 = int(input("Spieler 2"))
    if spalteFrei(spalte2):
        spielfeldAktualisieren(spalte2, 2)
        spielfeldAusgeben()