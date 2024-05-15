'''5. Eine Person hat 2 Telefonnummern. Es ist eine Liste mit den beiden Telefonnummern zu 
erstellen und anschließend der bestehende Eintrag Telefon mit der Liste der 
Telefonnummern zu ersetzen. In einer Schleife sind nacheinander alle Elemente als Schlüssel
Werte-Paar auszugeben.'''

# Das Personen-Dictionary mit den Vornamen und Alter
personen = {
    'Janis': {'Alter': 35, 'Geburtsjahr': 1986, 'Telefon': '0151 111111'},
    'Dimitri': {'Alter': 69, 'Geburtsjahr': 1953, 'Telefon': '0160 222222'},
    'Chucky': {'Alter': 89, 'Geburtsjahr': 1933, 'Telefon': '0171 333333'},
    'Tommy': {'Alter': 12, 'Geburtsjahr': 2012, 'Telefon': '0152 444444'},
    'Sarah': {'Alter': 28, 'Geburtsjahr': 1996, 'Telefon': '0163 555555'}
}

# Eine Liste mit den beiden neuen Telefonnummern erstellen
neue_telefonnummern = ['0172 666666', '0180 777777']

# Telefonnummern der Person "Janis" durch die neue Liste ersetzen
personen['Janis']['Telefon'] = neue_telefonnummern

# Alle Schlüssel-Werte-Paare nacheinander ausgeben
print("Schlüssel-Werte-Paare:")
for name, data in personen.items():
    print(f"Name: {name}")
    for key, value in data.items():
        print(f"{key}: {value}")
    print()