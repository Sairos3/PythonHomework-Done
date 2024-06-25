'''
Aufgabe

1.Datei einlesen
In einer Datei stehen zeilenweise die Länder 
(z.B. Italien, Frankreich, Spanien und Belgien)
Diese Datei ist einzulesen und auf der Konsole auszugeben

2.Datei einlesen und Konsoleingabe
Für alle gelesenen Länder ist in einer Schleife die Eingabe 
der jeweiligen Hauptstadt über die Konsole anzufordern. 
In einer Variablen von Datentyp Dictionary sind Land und Hauptstadt
anzulegen und dann auf der Konsole zu protokollieren.

3.Weitere Ausbaustufe:
Über einen Dialog sind zwei weitere Länder mit ihren Hauptstädten zum bestehenden
Dictionary zu ergänzen.
Das Dictionary ist in einer neuen Datei auszugeben, z.B.:
Italien Rom
Frankreich Paris
Spanien Madrid
Belgien Brüssel
usw.

4.Dateien vergleichen
Die Datei der Aufgabe 1 und die neue Datei, erstellt in der Aufgabe 3, 
sind jeweils einzulesen. Durch Abgleich der Datensätze soll ermittelt werden, 
welche Länder (über die Aufgabe 2)ergänzt wurden. 
Diese Länder sind auf der Konsole zu protokollieren
'''
############################################################
#----1.Datei einlesen----
# Drucken einer Nachricht, dass der erste Schritt beginnt
print('\n-1. Datei einlesen -')

# Definition der Funktion, die eine Datei liest
def read_file(filename):
    try:
        # Versuch, die Datei im Lesemodus zu öffnen
        with open(filename, 'r') as file:
            # Lesen des gesamten Datei-Inhalts
            content = file.read()
            
            # Splitten des Inhalts nach Kommas und Entfernen von Leerzeichen um die Ländernamen
            countries = [country.strip() for country in content.split(',')]
            
            # Aufzählen der Länder, beginnend mit Index 1
            for index, country in enumerate(countries, start=1):
                # Drucken der aufgezählten Länder
                print(f"{index}. {country}")
            
            # Rückgabe der Liste der Länder
            return countries
        
    # Behandlung des Falls, wenn die Datei nicht gefunden wird
    except FileNotFoundError as error:
        # Drucken einer Fehlermeldung
        print('Datei nicht gefunden:', error.args[1])
        # Beenden des Programms mit Statuscode 99
        exit(99)

# Aufruf der Funktion mit dem Dateinamen und Speichern der Rückgabe in der Variablen 'countries'
countries = read_file('Datei einlasen_HA_Lands.txt')

############################################################
#----2.Datei einlesen und Konsoleingabe----
print('\n-2. Datei einlesen und Konsoleingabe -')

# Definition der Funktion, die die Hauptstädte abfragt
def get_capitals(countries):
    # Initialisieren eines leeren Wörterbuchs
    capitals = {}
    # Iterieren über die Liste der Länder
    for country in countries:
        # Eingabe der Hauptstadt für das aktuelle Land
        capital = input(f"Geben Sie die Hauptstadt von {country} ein: ")
        # Speichern des Land-Hauptstadt-Paares im Wörterbuch
        capitals[country] = capital
    # Rückgabe des Wörterbuchs mit den Land-Hauptstadt-Paaren
    return capitals

# Definition der Hauptfunktion, die den Ablauf steuert
def main():
    # Festlegen des Dateinamens
    filename = 'Datei einlasen_HA_Lands.txt'
    # Einlesen der Datei und Speichern der Länder in der Variablen 'countries'
    countries = read_file(filename)
    # Abfragen der Hauptstädte für jedes Land und Speichern in der Variablen 'capitals'
    capitals = get_capitals(countries)

    # Drucken einer Nachricht, dass die Länder und ihre Hauptstädte protokolliert werden
    print("\nLänder und ihre Hauptstädte:")
    # Iterieren über die Land-Hauptstadt-Paare im Wörterbuch
    for country, capital in capitals.items():
        # Drucken jedes Land-Hauptstadt-Paares
        # Wenn der Ländernamen kürzer als 15 Zeichen ist, werden die restlichen Zeichen mit Leerzeichen aufgefüllt. 
        print(f"{country:15}: {capital}")

    # Hinzufügen von zwei weiteren Ländern und Hauptstädten
    add_more_countries(capitals)
    # Drucken einer Nachricht, dass die Länder und ihre Hauptstädte protokolliert werden
    print("\nAktualisierte Länder und ihre Hauptstädte:")
    # Iterieren über die Land-Hauptstadt-Paare im aktualisierten Wörterbuch
    for country, capital in capitals.items():
        # Drucken jedes Land-Hauptstadt-Paares
        print(f"{country:15}: {capital}")

    # Speichern des Wörterbuchs in eine neue Datei
    save_to_file(capitals, 'Lands_with_capitals.txt')

############################################################
#----3.Weitere Ausbaustufe----
print('\n-3.Weitere Ausbaustufe -')
'''     Line 100-109   '''
# Definition der Funktion, die das Wörterbuch in eine Datei schreibt
def save_to_file(capitals, filename):
    try:
        # Öffnen der Datei im Schreibmodus
        with open(filename, 'w') as file:
            # Iterieren über jedes Land-Hauptstadt-Paar im Wörterbuch
            for country, capital in capitals.items():
                # Schreiben des Land-Hauptstadt-Paares in die Datei
                file.write(f"{country} {capital}\n")
        # Drucken einer Bestätigungsmeldung
        print(f"Das Wörterbuch wurde erfolgreich in die Datei '{filename}' gespeichert.")
    except IOError as e:
        # Drucken einer Fehlermeldung, wenn die Datei nicht gespeichert werden kann
        print(f"Fehler beim Speichern der Datei '{filename}': {e}")

# Definition der Funktion, um zwei weitere Länder und Hauptstädte hinzuzufügen
def add_more_countries(capitals):
    for _ in range(2):  # Schleife für zwei Eingaben
        # Eingabe des neuen Landes
        country = input("Geben Sie ein weiteres Land ein: ")
        # Eingabe der Hauptstadt des neuen Landes
        capital = input(f"Geben Sie die Hauptstadt von {country} ein: ")
        # Hinzufügen des neuen Land-Hauptstadt-Paares zum Wörterbuch
        capitals[country] = capital

# Definition der Funktion, um zwei weitere Länder und Hauptstädte hinzuzufügen

############################################################
#----4.Dateien vergleichen----
print('\n-4.Dateien vergleichen -')




# Überprüfen, ob das Skript direkt ausgeführt wird, und die Hauptfunktion aufrufen
if __name__ == "__main__":
    main()