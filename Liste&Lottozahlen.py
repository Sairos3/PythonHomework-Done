'''
1. Es ist eine Liste mit 100 zufälligen ganzzahligen Werten 
im Bereich von 1 bis 1000 zu füllen. 
2. Die nächsten Lottozahlen sind zu „ermitteln“. 
Es ist eine Liste mit 6 zufälligen Ganzzahlen aus 
dem Bereich von 1 bis 49 zu füllen; 
bei den ermittelten Ganzzahlen sollte es keine Duplikate geben.
'''
from random import randint, sample

# Aufgabe 1: Liste mit 100 zufälligen ganzzahligen Werten im Bereich von 1 bis 1000
random_integers = [randint(1, 1000) for _ in range(100)]
# Erzeugt eine Liste mit 100 zufälligen ganzzahligen Werten im Bereich von 1 bis 1000

print("Liste mit 100 zufälligen ganzzahligen Werten im Bereich von 1 bis 1000:")
print(random_integers)

# Aufgabe 2: Lottozahlen (6 zufällige Ganzzahlen aus dem Bereich von 1 bis 49 ohne Duplikate)
lotto_numbers = sample(range(1, 50), 6)
# Erzeugt eine Liste mit 6 zufälligen Ganzzahlen aus dem Bereich von 1 bis 49 ohne Duplikate

print("\nDie nächsten Lottozahlen:")
print(lotto_numbers)