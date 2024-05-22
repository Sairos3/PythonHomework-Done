'''Aufgabe 
1. Textanalyse 
der Text dieser Aufgabenstellung soll untersucht werden: 
o Für alle im Text vorkommenden Buchstaben soll die Anzahl ermittelt werden und 
diese Übersicht absteigend sortiert nach der Anzahl ausgegeben werden. 
o Eine weitere Untersuchung soll ermitteln, wie viele Vokale (a, e, i, o, u) im Text 
gefunden werden.'''

# Text dieser Aufgabenstellung soll untersucht werden
text = 'Für alle im Text vorkommenden Buchstaben soll die Anzahl ermittelt \
werden und diese Übersicht absteigend sortiert nach der Anzahl ausgegeben \
werden. Eine weitere Untersuchung soll ermitteln, wie viele Vokale \
(a, e, i, o, u) im Text gefunden werden'.lower()
#user_input = input('Text that needs to be analyzed: ').lower()  
                                            # ohne .lower() zählt auch groß buchstaben
# Dictionary
buchstabe_db = {}

# Zählen Buchstaben im Text
for buchstabe in text:
    if buchstabe.isalpha():                 # If das ein Alphabet buchstabe ist
        if buchstabe in buchstabe_db:       # Alphabet in abc datenbank
            buchstabe_db[buchstabe] += 1    # If buchstabe = True dann +1
        else:
            buchstabe_db[buchstabe] = 1     # If buchstabe = False dann pasiert nichts.

# Sortieren der Buchstaben
sort_menge = sorted(buchstabe_db.items(), key=lambda item: item[1], reverse=True)
#           key_lamda = gibt 2wert fur jedes tupel, reverse = Reihenfolge sortiert
# Ausgabe Buchstabe und Anzahl
print("Anzahl Buchstaben (absteigend sortiert):")
for buchst, menge in sort_menge:    # a: 1
    print(f"{buchst}: {menge}")   


############################################################################
# Zählen der Vokale im Text
vowels = "aeiou"
# Vovels seperat zu machen
vowel_menge = sum(buchstabe_db[vowel] for vowel in vowels if vowel in buchstabe_db)
#         summe von db->einzige vovel fur vovel im vovels wann vowel von db nimmt
# Ausgabe der Anzahl der Vokale
print("\nAnzahl von Vokale (a, e, i, o, u) im Text:", vowel_menge)


#############################################################################
vowel_liste = [(vowel, buchstabe_db[vowel]) for vowel in vowels if vowel in buchstabe_db]
# buchstabe und menge
for vowel, menge in vowel_liste:
    print(f'{vowel}: {menge}')
print('-'*40, '\nSortierte Vokale')

#############################################################################
# Sortierte Vowels
vowel_dict = {vowel: buchstabe_db[vowel] for vowel in vowels if vowel in buchstabe_db}
sort_vowel = sorted(vowel_dict.items(), key=lambda item: item[1], reverse=True)
for vowel, menge in sort_vowel:
    print(f'{vowel}: {menge}')
