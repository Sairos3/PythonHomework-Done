'''
Aufgabe 
1. Countdown 
Es ist eine Funktion zu definieren, die durch Aufruf der Funktion selbst von 
einem Startwert bis 0 herunterzählt und diese Werte auf der Konsole ausgibt. 
2. Messreihe 
Aus einer Messreihe wurden 100 ganzzahlige Werte in einer Liste gespeichert. Für die 
Messwerte sollen verschiedene statistische Kenndaten ermittelt werden: 
a. Berechnung des Minimums der Messwerte 
b. Berechnung des Maximums der Messwerte 
c. Berechnung des Medians der Messwerte 
Hinweis: der Wert aus der Mitte der sortierten Liste 
d. Berechnung der Spannweite der Messwerte 
Hinweis: der Abstand zwischen dem kleinsten und dem größten Wert 
e. Berechnung der mittleren Abweichung der Messwerte 
Hinweis: für alle Werte ist der positive Abstand zum Mittelwert zu bilden 
diese Abstände werden aufsummiert und durch die Anzahl der 
Werte geteilt 
Beispiel für 3 Werte: 
Werte  
Mittelwert 
3, 7, 2 
(3+7+2) / 3 = 4 
mittlere Abw. (|3-4|+|7-4|+|2-4|) / 3 = (1+3+2) / 3 = 2 
f. 
Berechnung des Wertes, der am häufigsten vorkommt 
Hinweis zur Erzeugung der 100 Messwerte: 
# Standardmodul random einbinden 
import random 
messwerte = random.choices(range(0,1000), k=100)
'''
#------------------1.-----------------------
print('\n-1. Countdown-')
import random
import time

def countdown(numbers):
    if numbers < 0:                         # Stop by 0 kann auch ==
        return
    else:
        time.sleep(0.05)                    # Delay
        print('This is Number: ', numbers)  # print after each step
        countdown(numbers - 1)              # each step takes -1
countdown(10)
#------------------1.1----------------------
print('\n-1. Countdown 1.1 -')
def countup(x,y):
    
    while x <= y:
        print(x)
        x += 1

countup(0, 10)
#------------------1.2----------------------
print('\n-1. Countdown 1.2 -')
def countdown1(start):
    if start >= 0:
        print(start)
        for i in range (10000000):           # alternative for time
            pass
        countdown1(start - 1)

countdown1(10)
#------------------1.3----------------------
print('\n-1. Countdown 1.3 -')
def forcountdown(x):
    for x in range(0, x+1)[::-1]:
        print(x)
        x-1
forcountdown(10)
#------------------2.-----------------------
print('\n-2. Messreihe-')
#messwerte = [3, 10]
messwerte = random.choices(range(0, 1000), k=100)
def statistische_Kenndaten(messwerte):
    #minimum = min(messwerte)    # a. Berechnung des Minimums der Messwerte
    minimum = messwerte[0]
    for wert in messwerte:
        if wert < minimum:
            minimum = wert

    #maximum = max(messwerte)    # b. Berechnung des Maximums der Messwerte
    maximum = messwerte[0]
    for wert in messwerte:
        if wert > maximum:
            maximum = wert
    
    # c. Berechnung des Medians der Messwerte
    sortierte_messwerte = sorted(messwerte)    
    laenge = len(sortierte_messwerte)
    # Mittelwert berechnen
    summe = 0
    for wert in messwerte:
        summe += wert
    median = summe / laenge  
    # d. Berechnung der Spannweite der Messwerte
    spannweite = maximum - minimum
    # e. Berechnung der mittleren Abweichung der Messwerte 
    mittelwert = sum(messwerte) / laenge
    mittlere_abweichung = sum(abs(x - mittelwert) for x in messwerte) / laenge

    return {
        'Minimum' : minimum,
        'Maximum' : maximum,
        'Median(Middle)' : median,         
        'Spannweite(Range)' : spannweite,   # max - min = abstand
        'Mittlere Abweichung' : mittlere_abweichung
    }

ergebnisse = statistische_Kenndaten(messwerte)
for was, wert in ergebnisse.items():
    print(f'{was} = {wert}')
