'''
4. Kartenspiel: 
Die Karten eines Skatspieles sind in einer Liste sortiert einzutragen; 
beginnend bei Karo7, Karo8, Karo9, Karo10, KaroBube, KaroDame, KaroKönig und KaroAs 
und dann folgend die jeweiligen Kartenwerte für Herz, Pik und Kreuz. 
Diese Liste ist auf der Konsole auszugeben. 
Anschließend ist die Liste mit den 32 Karten zu 
mischen und so wieder auf der Konsole auszugeben.
'''
from random import shuffle

# Aufgabe 4: Kartenspiel (Skatspiel)
suits_de = ['Karo', 'Herz', 'Pik', 'Kreuz']
suits_en = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
# Definiert die vier Farben des Skatspiels auf Deutsch und Englisch

values_de = ['7', '8', '9', '10', 'Bube', 'Dame', 'König', 'As']
values_en = ['7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
# Definiert die Kartenwerte des Skatspiels auf Deutsch und Englisch

# Erstellen des Skatdecks mit deutschen Namen
skat_deck_de = [f'{suit}{value}' for suit in suits_de for value in values_de]
print("\nSortiertes Skatspiel (Deutsch):")
print(skat_deck_de)
# Gibt die sortierte Liste der Karten auf Deutsch auf der Konsole aus

# Mischen des Skatdecks auf Deutsch
shuffle(skat_deck_de)
print("\nGemischtes Skatspiel (Deutsch):")
print(skat_deck_de)
# Gibt die gemischte Liste der Karten auf Deutsch auf der Konsole aus

# # Erstellen des Skatdecks mit englischen Namen
# skat_deck_en = [f'{suit}{value}' for suit in suits_en for value in values_en]
# print("\nSortiertes Skatspiel (Englisch):")
# print(skat_deck_en)
# # Gibt die sortierte Liste der Karten auf Englisch auf der Konsole aus

# # Mischen des Skatdecks auf Englisch
# shuffle(skat_deck_en)
# print("\nGemischtes Skatspiel (Englisch):")
# print(skat_deck_en)
# # Gibt die gemischte Liste der Karten auf Englisch auf der Konsole aus