'''
Aufgabe 
1. In einer CSV-Datei ist eine Adressübersicht abzuspeichern. 
In dieser Datei sind Name, Vorname, Strasse, PLZ, Wohnort, Geburtsdatum
und die Telefonnr von 5 Personen abzuspeichern. 
2. Diese CSV-Datei ist über den „Basiszugriff auf eine Textdatei“ einzulesen 
und die Einträge formatiert auf der Konsole auszugeben. 
3. Diese CSV-Datei ist über ein „reader-Objekt“ aus dem csv-Modul einzulesen
und die Einträge formatiert auf der Konsole auszugeben. 
4. Diese CSV-Datei ist über ein „readerDict-Objekt“ aus dem csv-Modul 
einzulesen und die Einträge formatiert auf der Konsole auszugeben. 
5. Die CSV-Datei ist um die Daten von zwei weiteren Personen zu ergänzen 
und über eines der Lesemodule (siehe Aufgabe 2 oder Aufgabe 3 oder Aufgabe 4) 
zu protokollieren
'''
import csv
# 1. In einer CSV-Datei ist eine Adressübersicht abzuspeichern.
# Persons
personen = [
    ["Name1", "Vorname1", "Strasse1", "PLZ1", "Wohnort1", "Geburtsdatum1", "Telefonnr1"],
    ["Name2", "Vorname2", "Strasse2", "PLZ2", "Wohnort2", "Geburtsdatum2", "Telefonnr2"],
    ["Name3", "Vorname3", "Strasse3", "PLZ3", "Wohnort3", "Geburtsdatum3", "Telefonnr3"],
    ["Name4", "Vorname4", "Strasse4", "PLZ4", "Wohnort4", "Geburtsdatum4", "Telefonnr4"],
    ["Name5", "Vorname5", "Strasse5", "PLZ5", "Wohnort5", "Geburtsdatum5", "Telefonnr5"]
]

# File name
csv_datei = "adressen.csv"
# newline=''    = doesnt skip the line
# mode='w'      = write mode
with open(csv_datei, mode='w', newline='') as file:
# csv.writer    = Creates a CSV writer object with specified parameters.
# writerow(): Writes a single row of data to the CSV file. AS Heading in HTML
# writerows(): Writes multiple rows of data to the CSV file. AS Paragraph in HTML
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["Name", "Vorname","Strasse", "PLZ", "Wohnort", "Geburtsdatum", "Telefonnr"])
    writer.writerows(personen)

print(f"Die Datei '{csv_datei}' wurde erfolgreich erstellt.")
# 2. Diese CSV-Datei ist über ein „reader-Objekt“ aus dem csv-Modul einzulesen
# und die Einträge formatiert auf der Konsole auszugeben. 
with open(csv_datei, mode='r', newline='') as file:
# Read lines in file
    zeilen = file.readlines()
    
# extract Heading
header = zeilen[0].strip().split(',')
    
# extract Paragraph
daten = [zeile.strip().split(',') for zeile in zeilen[1:]]
    
# Formatierter Ausgabetitel
print("Adressübersicht:")
    
# Ausgabe des Headers mit abstand
print("{:<6} {:<10} {:<10} {:<6} {:<10} {:<15} {:<15}".format(
    header[0], header[1], header[2], header[3], header[4], header[5], header[6]
))

# Ausgabe der Datenzeilen mit abstand

for person in daten:
    print("{:<6} {:<10} {:<10} {:<6} {:<10} {:<15} {:<15}".format(
        person[0], person[1], person[2], person[3], person[4], person[5], person[6]
    ))
# 3. Diese CSV-Datei ist über ein „reader-Objekt“ aus dem csv-Modul einzulesen
# und die Einträge formatiert auf der Konsole auszugeben.
print("\nLesen mit csv.reader:")
with open(csv_datei, mode='r', newline='') as file:
    reader = csv.reader(file, delimiter=',')
    header = next(reader)
    
    print("Adressübersicht:")
    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<15} {:<15}".format(
        header[0], header[1], header[2], header[3], header[4], header[5], header[6]
    ))
    for person in reader:
        print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<15} {:<15}".format(
            person[0], person[1], person[2], person[3], person[4], person[5], person[6]
        ))

# 4. Diese CSV-Datei ist über ein „readerDict-Objekt“ aus dem csv-Modul 
# einzulesen und die Einträge formatiert auf der Konsole auszugeben.
print("\nLesen mit csv.DictReader:")
with open(csv_datei, mode='r', newline='') as file:
    reader = csv.DictReader(file, delimiter=',')
    
    print("Adressübersicht:")
    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<15} {:<15}".format(
        "Name", "Vorname", "Strasse", "PLZ", "Wohnort", "Geburtsdatum", "Telefonnr"
    ))
    for person in reader:
        print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<15} {:<15}".format(
            person["Name"], person["Vorname"], person["Strasse"], person["PLZ"], person["Wohnort"], person["Geburtsdatum"], person["Telefonnr"]
        ))

# 5. Die CSV-Datei ist um die Daten von zwei weiteren Personen zu ergänzen 
# und über eines der Lesemodule (siehe Aufgabe 2 oder Aufgabe 3 oder Aufgabe 4) 
# zu protokollieren.
neue_personen = [
    ["Name6", "Vorname6", "Strasse6", "PLZ6", "Wohnort6", "Geburtsdatum6", "Telefonnr6"],
    ["Name7", "Vorname7", "Strasse7", "PLZ7", "Wohnort7", "Geburtsdatum7", "Telefonnr7"]
]

with open(csv_datei, mode='a', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerows(neue_personen)

print(f"\nDie Datei '{csv_datei}' wurde mit zwei weiteren Personen ergänzt.")

# Protokollierung mit csv.reader
print("\nAktualisierte Datei (Lesen mit csv.reader):")
with open(csv_datei, mode='r', newline='') as file:
    reader = csv.reader(file, delimiter=',')
    header = next(reader)
    
    print("Adressübersicht:")
    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<15} {:<15}".format(
        header[0], header[1], header[2], header[3], header[4], header[5], header[6]
    ))
    for person in reader:
        print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<15} {:<15}".format(
            person[0], person[1], person[2], person[3], person[4], person[5], person[6]
        ))