'''
Aufgabe 
3. Von der Konsole sind beliebig viele Elemente einzulesen und einer Liste hinzuzufügen 
Mit der Eingabe q soll die Eingabe beendet werden. 
Die Liste ist zur Kontrolle auszugeben; anschließend ist die Liste sortiert auszugeben
'''

print('-'*50)
liste = []      # Speichern platz
while True:     # loop für mehr eingeben
    user_input = input("Geben Sie Liste ein (q zum Beenden): ")
#   liste.append(user_input)    = nimmt q mit im ausgabe vor if geshrieben
    if user_input == 'q':
        break
    liste.append(user_input)    # speichern eingabe in liste

print(liste)
sortiere = sorted(liste)
print(sortiere)
print('-'*20)
    #-------------------------
# or






