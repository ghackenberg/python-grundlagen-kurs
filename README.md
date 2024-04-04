# **Python** Grundlagen Kurs

![Vorschaubild](./Grafiken/LibreOffice/Vorschaubild.png)

Dieses Repository enthält Unterlagen für einen Python-Kurs, den wir an der [Fakultät für Technik und angewandte Naturwissenschaften](https://www.fh-ooe.at/campus-wels/) der [Fachhochschule Oberösterreich](https://www.fh-ooe.at) für Einsteiger in unterschiedlichen Studiengängen und -richtungen unterrichten.

Dieses Dokument ist wie folgt gegliedert:

- 🎯 **Lernziele** - wann sollte ich den Kurs machen?
- ⚙️ **Vorbereitungen** - wie muss ich meine Lernumgebung einrichten?
- 📦 **Lerneinheiten** - wie ist der Ablauf des Kurses gegliedert?

## 🎯 Lernziele

Der Kurs hat die folgenden Lernziele:

- Fähigkeit entwickeln, Programme in der Programmiersprache Python **lesen und interpretieren** zu können
- Fähigkeit entwickeln, einfache Programme mit der Programmiersprache Python **selbst realisieren** zu können

## ⚙️ Vorbereitungen

So richtest du deine Lernumgebung ein:

1. **[Python installieren](./Vorbereitungen/01_Python/README.md)**
1. **[Visual Studio Code installieren](./Vorbereitungen/02_Visual_Studio_Code/README.md)**
1. **[Visual Studio Code Erweiterungen installieren](./Vorbereitungen/03_Visual_Studio_Code_Erweiterungen/README.md)**
1. **[Jupyter Kernel installieren](./Vorbereitungen/04_Jupyter_Kernel/README.md)**

## 📋 Lerneinheiten

Der Kurs umfasst die folgenden Lerneinheiten:

1. **[Programme und Daten](./Lerneinheiten/Einheit_00/README.ipynb)**
   - Programme
     - Grundlegende Programmdefinition
     - Erweiterte Programmdefinition
     - Allgemeine Programmdefinition
   - Daten
     - Wahrheitswerte
     - Zahlen
     - Zeichenketten
1. **[Grundlegende Python-Syntax](./Lerneinheiten/Einheit_01/README.ipynb)**
   - Kommentare
     - ``# ...``
   - Literale
     - ``True``, ``False``, ``5``, ``5.5``, ``"..."``
   - Operatoren
     - ``not``, ``and``, ``+``, ``*``
   - Variablen
     - ``x = ...``
   - Funktionen und Funktionsaufrufe
     - ``type(...)``
     - ``print(...)``
     - ``input(...)``
     - ``open(...)``
   - Objektmethoden und Methodenaufrufe
     - ``f.read(...)``
     - ``f.readline()``
     - ``f.write(...)``
     - ``f.close()``
1. **[Datentypen und Operatoren / Funktionen](./Lerneinheiten/Einheit_02/README.ipynb)**
   - Datentypen
     - ``bool``
     - ``int``, ``float`` und ``complex``
     - ``list``, ``tuple`` und ``range``
     - ``str``
     - ``set`` und ``frozenset``
     - ``dict``
   - Operatoren
     - Boolsche Operatoren
     - Arithmetische Operatoren
     - Bitweise Operatoren
1. **[Verzweigungen und Schleifen](./Lerneinheiten/Einheit_03/README.ipynb)**
   - Verzweigungen
     - ``if ... elif ... else ...``
     - ``match ... case ...``
     - ``try ... throw ... catch ...``
   - Schleifen
     - ``for ...``
     - ``while ...``
1. **[Funktionsdefinitionen und Funktionsaufrufe](./Lerneinheiten/Einheit_04/README.ipynb)**
   - Funktionsdefinitionen
     - Signatur (Name, Parameter, Typenhinweise, Standardwerte)
     - Körper (``return ... throw ...``)
   - Funktionsaufrufe
     - Positionsparameter
     - Schlüsselwortparameter
     - *evtl. Rekursion*
1. **[Klassendefinitionen und Instanziierung](./Lerneinheiten/Einheit_05/README.ipynb)**
   - Definitionen
     - ``class X``
   - Instanzen
     - ``x = X(...)``
   - Konstruktoren
     - ``def __init__(self, ...)``
   - Felder
     - ``self.x = ...``
   - Methoden
     - ``def x(self, ...)``
   - Vererbung
     - ``class X(Y)``
   - Überschreibung
     - ``super()``
1. **[Module und Kapselung](./Lerneinheiten/Einheit_06/README.ipynb)**
   - ``export ...``
   - ``import ...``
   - ``__init__.py``
   - ``pip install ...``
1. **[Datenanalyse und -visualisierung](./Lerneinheiten/Einheit_07/README.ipynb)**
   - ``matplotlib``
   - ``numpy``
   - ``scipy``
   - ``pandas``
1. **[Grafische Benutzerschnittstellen](./Lerneinheiten/Einheit_08/README.ipynb)**
   - ``tkinter``