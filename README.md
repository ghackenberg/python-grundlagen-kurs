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

1. **[Grundlegende Definitionen](./Lerneinheiten/Einheit_00/README.ipynb)**
   - **Computer**
     - Von-Neumann-Architektur
     - Von-Neumann-Zyklus
   - **Befehle**
     - Speicherbefehle
     - Logische Befehle
     - Arithmetische Befehle
     - Sprungbefehle
   - **Daten**
     - Wahrheitswerte
     - Zahlen
     - Zeichenketten
   - **Programme**
     - Grundlegende Programmdefinition
     - Erweiterte Programmdefinition
     - Allgemeine Programmdefinition
1. **[Grundlegende Python-Syntax](./Lerneinheiten/Einheit_01/README.ipynb)**
   - **Kommentare**
     - ``# ...``
   - **Literale**
     - Wahrheitswerte: ``True`` und ``False``
     - Zahlen: ``5``, ``5.5`` und `5j`
     - Zeichenketten: ``"..."``
   - **Operatoren**
     - Wahrheitswerte: ``not ...``, ``... and ...``, ``... or ...``
     - Zahlen: ``... + ...``, `... - ...`, ``... * ...``, `... / ...`, `... // ...` und `... % ...`
     - Zeichenketten: ``"..." + "..."`` und ``f"..."``
   - **Variablen**
     - ``x = ...``
   - **Funktionsaufrufe**
     - ``type(...)``
     - ``print(...)``
     - ``input(...)``
     - ``open(...)``
   - **Methodenaufrufe**
     - ``f.read(...)``
     - ``f.readline()``
     - ``f.write(...)``
     - ``f.close()``
   - **Importe**
     - `import ...`
1. **[Komplexe Datentypen](./Lerneinheiten/Einheit_02/README.ipynb)**
   - **Sammlungen**
     - Sequenzen:
       - Datensequenzen: ``list``, ``tuple`` und ``range``
       - Zeichenketten: ``str``
       - Bytesequenzen: ``bytes``, `bytearray`, `memoryview`
     - Mengen: ``set`` und ``frozenset``
     - Abbildungen: ``dict``
   - **Klassen**
     - ``class``
1. **[Verzweigungen und Schleifen](./Lerneinheiten/Einheit_03/README.ipynb)**
   - **Verzweigungen**
     - ``if ... elif ... else ...``
     - ``match ... case ...``
     - ``try ... throw ... catch ...``
   - **Schleifen**
     - ``for ...``
     - ``while ...``
1. **[Funktionsdefinitionen und Funktionsaufrufe](./Lerneinheiten/Einheit_04/README.ipynb)**
   - **Funktionsdefinitionen**
     - Signatur (Name, Parameter, Typenhinweise, Standardwerte)
     - Körper (``return ... throw ...``)
   - **Funktionsaufrufe**
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