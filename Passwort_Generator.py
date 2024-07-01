'''
3. Passwort-Generator: Es ist ein 16-stelliges Passwort zu generieren; 
es dürfen alle druckbaren Zeichen, also Groß- und Kleinbuchstaben, 
Ziffern und die Sonderzeichen vorhanden sein. 
'''
from random import choice
# Importiert die Funktion choice aus dem random-Modul, 
# die verwendet wird, um zufällig ein Element aus einer Sequenz auszuwählen.

from string import ascii_letters, digits, punctuation
# Importiert die Zeichenketten ascii_letters, 
# digits und punctuation aus dem string-Modul.

# ascii_letters enthält alle Groß- und Kleinbuchstaben des ASCII-Alphabets.
# digits enthält alle Ziffern (0-9).
# punctuation enthält alle druckbaren Satzzeichen.

# Aufgabe 3: Passwort-Generator (16-stelliges Passwort mit allen druckbaren Zeichen)
password_characters = ascii_letters + digits + punctuation
# Erstellt eine Zeichenkette, die alle druckbaren Zeichen enthält, 
# indem ascii_letters, digits und punctuation zusammengefügt werden.

password = ''.join(choice(password_characters) for _ in range(16))
# Generiert ein 16-stelliges Passwort. 
# Dazu wird eine Liste von 16 zufälligen Zeichen aus password_characters erstellt.

# choice(password_characters) wählt zufällig ein Zeichen aus password_characters aus.
# Die join-Methode fügt die 16 zufällig ausgewählten Zeichen zu einem einzigen String zusammen.

print("\nGeneriertes Passwort:")
# Gibt eine neue Zeile und die Zeichenkette "Generiertes Passwort:" aus.

print(password)
# Gibt das generierte Passwort aus.


'''
import random
import string

password_characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(password_characters) for _ in range(16))
print("\nGeneriertes Passwort:")
print(password)
'''