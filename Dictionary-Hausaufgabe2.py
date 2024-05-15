'''
2. Eine Person hatte Geburtstag und das Alter dieser Person soll um 1 erhöht werden. Das 
Schlüssel-Werte-Paar zu dieser Person soll vor und nach der Änderung ausgegeben werden.  
'''

# Dictionary mit Vornamen und Alter erstellen
personen = {
    'Janis': 35,
    'Dimitri': 69,
    'Chucky': 89,
    'Tommy': 12,
    'Sarah': 28,
}
# Name der Person, die Geburtstag hatte
person_name = 'Janis'

# Alter der Person vor der Erhöhung ausgeben
print(f"Alter von {person_name} vor dem Geburtstag:", personen[person_name])

# Alter der Person um 1 erhöhen
personen[person_name] += 1

# Alter der Person nach der Erhöhung ausgeben
print(f"Alter von {person_name} nach dem Geburtstag:", personen[person_name])