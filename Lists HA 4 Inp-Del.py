'''
Aufgabe 
4. Erstelle eine Liste mit den Namen von fünf Großstädten. Diese Liste ist sortiert auszugeben. 
Über die Konsole sollen anschließend zwei weitere Städte zur Eingabe angefordert werden 
und zur Liste hinzugefügt werden. Diese Liste, nun mit 7 Städtenamen, ist wieder zu sortieren 
und anschließend in umgekehrter Reihenfolge auszugeben. Im nächsten Schritt werden die 
erste und die letzte Stadt aus der Liste entfernt und die reduzierte Liste ausgegeben. 
'''
staedte = ['Berlin', 'Hamburg', 'München', 'Köln', 'Frankfurt']
staedte.sort()      # Sort
print("Sortierte Liste der Großstädte:", staedte)

# Eingabe von zwei weiteren Städten
for _ in range(2):  #2x input
    stadt = input("Bitte geben Sie eine weitere Stadt ein: ")
    staedte.append(stadt)       # update stadte
    

# Sortieren und Ausgeben der Liste in umgekehrter Reihenfolge
staedte.sort()      # Sort
print("Sortierte Liste mit sieben Städtenamen in umgekehrter Reihenfolge:", staedte[::-1])

# Entfernen der ersten und letzten Stadt aus der Liste
del staedte[0]  # Entfernt die erste Stadt
del staedte[-1]  # Entfernt die letzte Stadt

# Ausgeben der reduzierten Liste
print("Reduzierte Liste nach Entfernen der ersten und letzten Stadt:", staedte)






