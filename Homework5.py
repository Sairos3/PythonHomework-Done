'''
Aufgabe 
1. Visitenkarte 
über die Konsole werden die Personendaten (Vorname, Nachname, Straße, Ort und 
Telefonnr.) erfasst 
Diese Daten sind wie folgt auszugeben: 
Name: Heinrich Müller 
Strasse: Luisenstr. 5 
Ort: Düsseldorf
Telefon: 123456
'''
print('-'*100)
# Visitkarte_1
Vorname = 'Heinrich'
Nachname = 'Müller'
Straße = 'Luisenstr. 5'
Ort = 'Düsseldorf'
Telefonnr = '123456'

print('Name: ', ' ' * 6, Vorname , Nachname)
print('Strasse: ', ' ' * 3, Straße)
print('Ort: ', ' ' * 7, Ort)
print('Telefonnr: ', ' ' * 1, Telefonnr)
print('-'*100)
# Visitkarte_2
Answer = [Vorname +' '+Nachname, Straße, Ort, Telefonnr]
Question = 'Name:', 'Strasse:', 'Ort:', 'Telefonnr:'

for QL, value in enumerate(Answer):
    print(Question[QL], ' ' * (12 - len(Question[QL])), value)
print('-'*100)
# Visitkarte_3
'''
Vorname = 'Heinrich'
Nachname = 'Müller'
Straße = 'Luisenstr. 5'
Ort = 'Düsseldorf'
Telefonnr = '123456'
'''
print('Name:', f'{Vorname:>16} {Nachname:>1}')
print('Strasse:', f'{Straße:>17}')
print('Ort:', f'{Ort:>19}')
print('Telefonnr:', f'{Telefonnr:>9}')
print('-'*100)
# Visitkarte_4
print(f'{'Name:':13} {Vorname} {Nachname}')
print(f'{'Stasse:':13} {Straße}')
print(f'{'Ort:':13} {Ort}')
print(f'{'Telefon:':13} {Telefonnr}')
print('-'*100)
# Visitkarte_5
Vorname = 'Heinrich'
Nachname = 'Müller'
Straße = 'Luisenstr. 5'
Ort = 'Düsseldorf'
Telefonnr = '123456'

Answer = [Vorname +' '+Nachname, Straße, Ort, Telefonnr]
Question = 'Name:', 'Strasse:', 'Ort:', 'Telefonnr:'

for QL, value in enumerate(Answer):
    print(QL, value)
print('-'*100)

