'''
3. Alle Namen der Personen sollen ohne Alter auf der Konsole ausgegeben werden.  
'''

# Dictionary mit Vornamen und Alter erstellen
personen = {
    'Janis': 35,
    'Dimitri': 69,
    'Chucky': 89,
    'Tommy': 12,
    'Sarah': 28,
}

# Alle Namen der Personen auf der Konsole ausgeben
print("Namen der Personen:")
for name in personen:
    print(name)
print('-'*20)

for alter in personen.values():
    print(alter)