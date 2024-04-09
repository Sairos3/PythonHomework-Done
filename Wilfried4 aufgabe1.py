Geschlecht = input('Geben Sie Ihr Geschlecht ein (M, W, D): ')
uhrzeit = int(input('Bitte geben Sie die aktuelle Uhrzeit in Stunden (0-24) an: '))

if Geschlecht == 'M':
    anrede = 'Herr'
elif Geschlecht == 'W':
    anrede = 'Frau'
elif Geschlecht == 'D':
    anrede = 'Diverse'
else:
    print('Ungültiges Geschlecht. Bitte geben Sie M, W oder D ein.')
    exit()

if 0 <= uhrzeit < 6:
    greeting = "Guten Nacht"
elif 6 <= uhrzeit < 12:
    greeting = "Guten Morgen"
elif 12 <= uhrzeit < 18:
    greeting = "Guten Tag"
elif 18 <= uhrzeit < 24:
    greeting = "Guten Abend"
else:
    print('Ungültige Uhrzeit. Bitte geben Sie eine Zahl zwischen 0 und 24 an.')
    exit()

print(f'{greeting}, {anrede}!')