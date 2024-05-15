'''
1. Tupel erstellen und ausgeben 
es ist ein Tupel mit 5 Obstsorten (Datentyp str) zu erstellen und auf der Konsole auszugeben 
'''

# Tupel mit 5 Obstsorten erstellen
obstsorten = ('Apfel', 'Banane', 'Orange', 'Erdbeere', 'Kiwi')

# Tupel auf der Konsole ausgeben
print("Die Obstsorten sind:")
for obst in obstsorten:
    print(obst)
print('-'*20)

'''
2. weitere Tupel 
zwei weitere Tupel sind zu erstellen, das eine enthält 4 Milchprodukte und einem leeren 
String, das andere 2 Backwaren. Beide Tupel sind auf der Konsole nacheinander auszugeben. 
'''

# Tupel mit 4 Milchprodukten und einem leeren String erstellen
milchprodukte = ('Milch', 'Käse', 'Joghurt', 'Butter', '')

# Tupel mit 2 Backwaren erstellen
backwaren = ('Brot', 'Kuchen')

# Tupel mit Milchprodukten auf der Konsole ausgeben
print("Die Milchprodukte sind:")
for produkt in milchprodukte:
    print(produkt)

# Tupel mit Backwaren auf der Konsole ausgeben
print("Die Backwaren sind:")
for produkt in backwaren:
    print(produkt)
print('-'*20)
