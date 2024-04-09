# 1. Einmaleins der Zahl 9 ist über eine Schleife auf der Konsole auszugeben.

# 2. Fakultät, in der Mathematik geschrieben mit ! hinter der Zahl, ist definiert als
# 0!=1 , 1!=1 , 2!=2*1=2 , 3!=3*2*1=6 , n!=1*2*3*...*(n-1)*n
# Von der Konsole ist eine Zahl einzulesn, für die über eine Schleife die Fakultät
# berechnet und ausgegeben wird.

# 3. Es ist ein Programm zur Kapitalberechnung zu erstellen.
# Über die Konsole werden das Anfangskapital und der Zinssatz zur Eingabe angefordert.
# Es ist das Endkapital nach einem und nach 2 Jahr zu mit der foglenden Formel zu berechnen:
# k1=k0*((p/100)+1) , k0=Anfangskapital , p=Zinssatz
# Zur Berechnung des Endkapitals des zweiten Jahrs nimmt man das Endkapital von ersten Jahr als Anfangskapital.

######################################################################
#1
zahl = 8
for i in range(1, 11):  # Eingabe *(1-10)
    print(f"{zahl} * {i} = {zahl * i}")

######################################################################
#2
zahl2 = int(input("Geben Sie eine Zahl ein: "))

def berechne_fakultaet(n):
    fakultaet = 1
    for i in range(1, n + 1):
        fakultaet *= i # Eingabe = 3 = 1*1+1*2+1*3
    return fakultaet

print(f"Die Fakultät von {zahl2} ist {berechne_fakultaet(zahl2)}")

######################################################################
#3
# Anfangskapital und Zinssatz von der Konsole einlesen
# AK=Anfangskapital     j1=Jahr1        j2=Jahr2
ak = float(input("Geben Sie das Anfangskapital ein: "))
p = float(input("Geben Sie den Zinssatz in Prozent ein: "))

# Funktion zur Berechnung des Endkapitals nach einem Jahr
def Jahr1(ak, p):
    return ak * ((p / 100) + 1)

# Funktion zur Berechnung des Endkapitals nach zwei Jahren
def Jahr2(k1, p):
    return k1 * ((p / 100) + 1)

# Endkapital nach einem Jahr berechnen
j1 = Jahr1(ak, p)
print(f"Endkapital nach einem Jahr: {j1:.2f} €")

# Endkapital nach zwei Jahren berechnen
j2 = Jahr2(j1, p)
print(f"Endkapital nach zwei Jahren: {j2:.2f} €")
# {k2:.2f} k2 = Jahr2(k1, p), :.2f = float mit 2 nach kommastellen
