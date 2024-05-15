'''
1. Ein Dictionary mit den Vornamen und dem Alter (Ganzzahl) von 5 Personen ist zu erstellen. 
Der Vorname ist der Schlüssel und das Alter der Wert in diesem Dictionary. 
Das Dictionary ist als Ganzes auf der Konsole auszugeben. Anschließend sind in einer Schleife 
nacheinander alle Elemente als Schlüssel-Werte-Paar auszugeben. 
'''

# Dictionary mit Vornamen und Alter erstellen
personen = {
    'Janis': 35,
    'Dimitri': 69,
    'Chucky': 89,
    'Tommy': 12,
    'Sarah': 28,
#'Name': Alter
}

# Das gesamte Dictionary auf der Konsole ausgeben
print("Das Dictionary mit den Personen ist:", personen)

# Alle Elemente des Dictionarys nacheinander ausgeben
print("\nAusgabe der einzelnen Schlüssel-Werte-Paare:")
for name, alter in personen.items():
    print(f"Name: {name}, Alter: {alter}")
