'''
Aufgabe 
1. Es sind Datumsdifferenzen zu berechnen: 
o 01.01.2020 bis heute 
o 01.07.2022 bis 30.09.2022 
o Beide Datumsangaben über die Konsole einlesen und die Differenz ermitteln
'''
print('\n-1. Es sind Datumsdifferenzen zu berechnen-')
from datetime import datetime
# 1. Berechnung der Differenz zwischen dem 01.01.2020 und heute
# Ein datum
datum1 = datetime(2020, 1, 1)
# datum zurzeit
heute = datetime.now()
# Differenze
differenz1 = heute - datum1
print(f"Differenz 01.01.2020 bis heute ({heute.strftime('%d.%m.%Y')}) beträgt {differenz1.days} Tage.")

# 2. Berechnung der Differenz zwischen dem 01.07.2022 und dem 30.09.2022
# Ein datum
datum2 = datetime(2022, 7, 1)
# Zweites datum
datum3 = datetime(2022, 9, 30)
# Differenz
differenz2 = datum3 - datum2
# Differenz as days
print(f"Differenz 01.07.2022 bis 30.09.2022 beträgt {differenz2.days} Tage.")

'''
2. Die Laufzeit für die Ausführung einer Schleife ist zu ermitteln: 
o Es ist eine Schleife zu programmieren, die alle Zahlen von 1 bis 1000 addiert, deren 
Ausführungszeit ist zu ermitteln. 
o Eine weitere Schleife soll programmiert werden und die Zahlen von 1 bis 1.000.000 
addiert werden, wieder ist die Ausführungszeit zu ermitteln.
'''
print('\n-2. Die Laufzeit für die Ausführung einer Schleife ist zu ermitteln-') 
# Importiert das time-Modul, um die Zeit zu messen
import time
# Schleife zum Addieren der Zahlen von 1 bis 1000 und Ermittlung der Ausführungszeit
# Speichert den aktuellen Zeitpunkt vor Beginn der Schleife
start_time_1 = time.time()  
# Initialisiert die Summe auf 0
sum_1 = 0 
# Schleife von 1 bis 1000 (einschließlich) 
for i in range(1, 1001):  
# Addiert die aktuelle Zahl zur Summe
    sum_1 += i  
# Speichert den aktuellen Zeitpunkt nach Ende der Schleife
end_time_1 = time.time()  
# Berechnet die verstrichene Zeit als Differenz
elapsed_time_1 = end_time_1 - start_time_1  

print(f"Summe der Zahlen 1 bis 1000 beträgt {sum_1}.")  # Gibt die berechnete Summe aus
print(f"Ausführungszeit der Schleife (1 bis 1000) beträgt {elapsed_time_1:.6f} Sekunden.")  # Gibt die Ausführungszeit aus
print('\n')
start_time_2 = time.time()  
sum_2 = 0  
for i in range(1, 1000001):  
    sum_2 += i  
end_time_2 = time.time()  
elapsed_time_2 = end_time_2 - start_time_2  

print(f"Summe der Zahlen 1 bis 1.000.000 beträgt {sum_2}.")  # Gibt die berechnete Summe aus
print(f"Ausführungszeit der Schleife (1 bis 1.000.000) beträgt {elapsed_time_2:.6f} Sekunden.")  # Gibt die Ausführungszeit aus

'''
3. Für die Erfassung von Artikeln (z.B. Banane, Orange, Zitrone usw.) und deren Einzelpreis ist 
eine Endlosschleife zu programmieren; als Abbruchkriterium wird die Eingabe von „q“ bei der 
Artikeleingabe vorgeschlagen. 
Die Artikelbezeichnungen und die Einzelpreise sind zusammen mit einem Zeitstempel in 
einer Textdatei abzuspeichern. 
'''
print('\n-3. Für die Erfassung von Artikeln (z.B. Banane, Orange, Zitrone usw.)') 
# Importiert das time-Modul, um Zeitstempel zu erzeugen
import time  
# Dateiname für die Speicherung der Artikel
datei_name = "Datum_Time_DB3.txt"
# Endlosschleife zur Erfassung von Artikeln und Preisen
while True:
# Erfasst den Artikel
    artikel = input("Geben Sie den Artikel ein (oder 'q' zum Beenden): ")  
# Überprüft, ob der Benutzer 'q' zum Beenden eingegeben hat
    if artikel.lower() == 'q': 
# Beendet die Schleife 
        break
# Erfasst den Preis des Artikels
    while True:                             ######ADD######
        preis = input("Geben Sie den Einzelpreis ein: ") 
# Ersetzt Komma durch Punkt in der Preiseingabe
        preis = preis.replace(',', '.')     ######ADD######
        try:
# Versucht, den Preis in eine Fließkommazahl umzuwandeln
            preis = float(preis)
            break
        except ValueError:
# Gibt eine Fehlermeldung bei ungültigem Preis aus
            print("Ungültiger Preis. Bitte geben Sie eine Zahl ein.")  
# Erzeugt einen Zeitstempel
    zeitstempel = time.strftime("%Y-%m-%d %H:%M:%S")

# Speichert Artikel, Preis und Zeitstempel in der Textdatei
# Öffnet die Datei zum Anhängen von Daten ('a' für Anhangsmodus) und stellt sicher, 
# dass keine zusätzlichen Leerzeilen hinzugefügt werden (newline='')
    with open(datei_name, mode='a', newline='') as file:
        file.write(f"{zeitstempel}, {artikel}, {preis}\n")

    print(f"Artikel '{artikel}' mit Preis {preis} wurde gespeichert.")  # Bestätigt die Speicherung des Artikels

print("Erfassung beendet.")
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
        menge = input(f"Geben Sie die gewünschte Menge für {artikel} (Preis: {preis}): ")  # Abfrage der Menge
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