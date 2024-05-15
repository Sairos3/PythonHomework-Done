'''  
4. Für alle Personen im Dictionary soll auch die Telefonnummer ergänzt werden. 
Dazu kann ein weiteres Dictionary angelegt werden, in dem die Schlüssel Geburtsjahr und 
Telefon verwendet werden, z.B. {"Geburtsjahr": 1985, "Telefon": "0151 23456"}. Mit diesen 
Angaben ist die Altersangabe zu überschreiben. Für die weiteren Personen sind diese 
Änderungen ebenfalls vorzunehmen. Das Personen-Dictionary ist komplett auszugeben. 
'''

# Neues Personen-Dictionary mit Vornamen und Alter
personen = {
    'Janis': 35,
    'Dimitri': 69,
    'Chucky': 89,
    'Tommy': 12,
    'Sarah': 28,
}

# Dictionary mit Telefonnummern und Geburtsjahren
telefonnummern = {
    'Janis': {"Geburtsjahr": 1986, "Telefon": "0151 111111"},
    'Dimitri': {"Geburtsjahr": 1953, "Telefon": "0160 222222"},
    'Chucky': {"Geburtsjahr": 1933, "Telefon": "0171 333333"},
    'Tommy': {"Geburtsjahr": 2012, "Telefon": "0152 444444"},
    'Sarah': {"Geburtsjahr": 1996, "Telefon": "0163 555555"}
}

# Aktualisierte Daten in das Personen-Dictionary einfügen
personen.update(telefonnummern)

# Komplettes Personen-Dictionary ausgeben
print("Das aktualisierte Personen-Dictionary ist:")
print(personen)
print('-'*20)
for name, data in personen.items():
    print(f"Name: {name},\n Geburtsjahr: {data['Geburtsjahr']},\n Telefon: {data['Telefon']}\n")
