'''
4. Lösung überarbeiten 
Folgende Aufgabe wurde bereits gelöst: 
Für eine Nachricht soll von einem Programm automatisch die Anrede formuliert werden. Von 
der Konsole sind Eingaben für Name, Geschlecht und die Uhrzeit als Stundenangabe 
einzulesen  Die Anrede soll je nach Tageszeit mit „Guten Morgen“ (0–9 Uhr), „Guten Tag“ 
(10–17), „Guten Abend (18–0 Uhr) beginnen und anschließend mit „Herr xxx“ bzw. „Frau xxx“ 
fortgesetzt werden. Für xxx soll der entsprechende Name eingesetzt werden 
Das Programm ist so anzupassen, dass die Überprüfung auf gültige Eingaben (wie z.B.: m, w, 
d, M, Mann, f, Frau, …) mit Hilfe eines Tupels der zugelassen Werte durchgeführt wird. 
Ebenfalls sollen die Begrüßungsformeln (Guten Morgen, Guten Tag und Guten Abend) in 
einem Tupel definiert werden und die Anrede mit entsprechenden Zugriffen daraus 
zugesetzt werden. 
'''

# Tupel für gültige Eingaben für Geschlecht
gueltige_eingaben = ('m', 'w', 'd', 'M', 'W', 'D', 'mann', 'frau')

# Tupel für Begrüßungsformeln je nach Tageszeit
begruessungsformeln = ('Guten Morgen', 'Guten Tag', 'Guten Abend')

# Eingaben vom Benutzer einlesen
name = input("Bitte geben Sie Ihren Namen ein: ")
geschlecht = input("Bitte geben Sie Ihr Geschlecht ein (m/w): ").lower()
uhrzeit = int(input("Bitte geben Sie die Uhrzeit als Stundenangabe ein (0-23): "))

# Überprüfen, ob die Eingabe für das Geschlecht gültig ist
if geschlecht not in gueltige_eingaben:
    print("Ungültige Eingabe für Geschlecht.")
    exit()

# Begrüßungsformel je nach Tageszeit auswählen
if 0 <= uhrzeit < 10:
    begruessung = begruessungsformeln[0]
elif 10 <= uhrzeit < 18:
    begruessung = begruessungsformeln[1]
else:
    begruessung = begruessungsformeln[2]

# Anrede basierend auf Geschlecht formulieren
if geschlecht in ('m', 'M', 'mann', 'Mann'):
    anrede = "Herr " + name
else:
    anrede = "Frau " + name

# Anrede mit Begrüßungsformel kombinieren und ausgeben
vollstaendige_anrede = f"{begruessung}, {anrede}."
print(vollstaendige_anrede)