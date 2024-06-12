'''
1. Umdrehen  
Es sind Funktionen zu definieren, mit denen die Reihenfolge der einzelnen Elemente 
in Zeichenketten, Listen, und Tupel umgedreht werden bzw. für Zahlen soll das
Vorzeichen umgedreht werden. 
Mit Testdaten der Datentypen Ganzzahl, Gleitpunktzahl, Zeichenkette,
Liste und Tupel soll 
getestet werden – auf der Konsole sind die Werte vor dem Umdrehen und nach dem 
Umdrehen auszugeben '''
#--------------------------STRING----------------------------------------
print('\n-STRING-')
def umgedreht_string(string):
    return string[::-1]

a_string = 'String'
print('Vor Umdrehen: ', (a_string))
print('Nach Umdrehen: ', (umgedreht_string(a_string)))
#--------------------------INTIGER----------------------------------------
'''1'''
print('\n-INTIGER:1-')
def umgedreht_intiger(intiger):
    return int(str(intiger)[::-1])

a_intiger = 12345
print('\nErste variant Intiger:')
print('Vor Umdrehen: ', (a_intiger))
print('Nach Umdrehen: ', (umgedreht_intiger(a_intiger)))
#------------------------------------------------------------------
'''2'''
print('\n-INTIGER:2-')
def umgedreht_negative_intiger(intiger):
    return -int(str(-intiger)[::-1])

b_intiger = -12345
print('\nZweite variant Intiger mit negative Ziffern:')
print('Vor Umdrehen: ', (b_intiger))
print('Nach Umdrehen: ', (umgedreht_negative_intiger(b_intiger)))
#------------------------------------------------------------------
'''3'''
print('\n-INTIGER:3-')
def if_umgedreht_intiger(intiger):
    if intiger > 0:
        return int(str(intiger)[::-1])
    else:
        return -int(str(-intiger)[::-1])
    
c_intiger = -12345
d_intiger = 12345
print('\nDrite variant Intiger mit if schleife + negative Ziffern:')
print('Vor Umdrehen: ', (c_intiger, d_intiger))
print('Nach Umdrehen: ', (if_umgedreht_intiger(c_intiger), \
(if_umgedreht_intiger(d_intiger))))
#------------------------------------------------------------------
'''4'''
print('\n-INTIGER:OMFG-')
def OMFG(intiger):
    minus = intiger < 0
    intigerx = 0
    intiger = abs(intiger)
    while intiger != 0:
        last_intiger = intiger % 10                 # decimal numeral system
        intiger = intiger // 10                     # decimal numeral system
        intigerx = intigerx * 10 + last_intiger     # decimal numeral system
    if minus:
        intigerx = -intigerx
    return intigerx

e_intiger = -12345 
g_intiger = 12345
print('\nI dont want to talk about this: ', (g_intiger))
print('Nach Umdrehen: ', (OMFG(g_intiger)))
#--------------------------LIST----------------------------------------
print('\n-LIST-')
list_intiger = [1, 2, 3, 4, 5]
minus_list_intiger = [-1, -2, -3, -4, -5]
def intiger_list(liste):
    # if (num < 0 for num in liste):
    #      return [num for num in liste[::-1]]
    return liste[::-1]
print(intiger_list(list_intiger))
print(intiger_list(minus_list_intiger))
#-------------------------TUPLE-----------------------------------------
print('\n-TUPEL-')
def umgedreht_tuple(tup):
    #return tuple(reversed(tup))
    return tuple(-x for x in reversed(tup))

test_tuple = (1, 2, 3, 4, 5)
print('\nTupel:', test_tuple)
print('Tupel:', umgedreht_tuple(test_tuple))
#-------------------------FLOAT-----------------------------------------
print('\n-FLOAT-')
def umgedreht_float(float_number):
    return float(str(float_number)[::-1])

test_float = 123.45
print('\nKommazahl:', test_float)
print('Kommazahl:', umgedreht_float(test_float))