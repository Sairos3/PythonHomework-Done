'''
3. mehrere Tupel zusammenfügen 
alle 3 Tupel sind in einem neuen Tupel zusammenzufügen. Auf der Konsole ist das Tupel 
selbst, sowie der Datentyp des Tupels (Hinweis: type() ) auszugeben. Weiterhin sind das erste 
und das letzte Element des Tupels sowie deren Typ auszugeben 
'''

# Erste Obstsorten
obstsorten = ('Apfel', 'Banane', 'Orange', 'Erdbeere', 'Kiwi')

# Milchprodukte und leere Zeichenfolge
milchprodukte = ('Milch', 'Käse', 'Joghurt', 'Butter', '')

# Backwaren
backwaren = ('Brot', 'Kuchen')

# Alle drei Tupel zusammenführen
alle_tupel = obstsorten + milchprodukte + backwaren

# Das kombinierte Tupel auf der Konsole ausgeben
print("Das kombinierte Tupel ist:", alle_tupel)

# Datentyp des kombinierten Tupels ausgeben
print("Der Datentyp des kombinierten Tupels ist:", type(alle_tupel))

# Das erste Element des kombinierten Tupels ausgeben
print("Das erste Element des kombinierten Tupels ist:", alle_tupel[0])

# Das letzte Element des kombinierten Tupels ausgeben
print("Das letzte Element des kombinierten Tupels ist:", alle_tupel[-1])

# Typ des ersten Elements des kombinierten Tupels ausgeben
print("Der Typ des ersten Elements des kombinierten Tupels ist:", type(alle_tupel[0]))

# Typ des letzten Elements des kombinierten Tupels ausgeben
print("Der Typ des letzten Elements des kombinierten Tupels ist:", type(alle_tupel[-1]))