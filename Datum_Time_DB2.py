'''
4. Mit einem weiteren Programm ist diese Datei einzulesen: 
Für alle Artikel ist die gewünschte 
Menge über die Konsol-Eingabe anzufordern. 
Es ist die Summe für jeden Artikel zu bilden 
(Einzelpreis * Menge) und der Gesamtbetrag zu errechnen 
und auf der Konsole auszugeben.
''' 
import csv  # Importiert das csv-Modul, um mit CSV-Dateien zu arbeiten

# Dateiname für die gespeicherten Artikel
datei_name = "Datum_Time_DB3.txt"

# Liste zum Speichern der Artikel und ihrer Preise
artikel_liste = []

# Einlesen der Datei und Speichern der Artikel in der Liste
with open(datei_name, mode='r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        zeitstempel, artikel, preis = row
        artikel_liste.append((artikel, float(preis)))  # Speichert Artikel und Preis als Tupel in der Liste

# Initialisierung der Variablen für den Gesamtbetrag
gesamtbetrag = 0

# Verarbeitung der Artikel, Abfrage der Menge und Berechnung der Summe
for artikel, preis in artikel_liste:
    while True:
        menge = input(f"Menge für {artikel} (Preis: {preis}): ")  # Abfrage der Menge
        try:
            menge = int(menge)  # Versucht, die Menge in eine Ganzzahl umzuwandeln
            break  # Bricht die Schleife ab, wenn die Konvertierung erfolgreich ist
        except ValueError:
            print("Ungültige Menge. Bitte geben Sie eine ganze Zahl ein.")  # Gibt eine Fehlermeldung bei ungültiger Menge aus
    
    artikel_summe = preis * menge  # Berechnet die Summe für den Artikel
    gesamtbetrag += artikel_summe  # Addiert die Artikelsumme zum Gesamtbetrag
    
    print(f"Summe für {artikel}: {artikel_summe:.2f}")  # Gibt die Summe für den Artikel aus

# Ausgabe des Gesamtbetrags
print(f"\nGesamtbetrag: {gesamtbetrag:.2f}")