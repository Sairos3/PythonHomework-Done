'''
Aufgabe 
2. Trenne eine Liste an einem Index in zwei Teillisten. 
Hinweis: Der Index beginnt bei 0. Getrennt wird vor dem Eintrag an der Indexstelle. Soll eine 
Liste an Index 0 getrennt werden, dann ist die erste Liste leer. 
Beispiel: [1,3,5,8,9,3] getrennt an Index 3 ergibt [1,3,5] [8,9,3] 
'''
list = [1,3,5,8,9,3]
def calculate (seperate):
    list1 = seperate[0:3]   # 0:3 = 1<->3
    list2 = seperate[3:6]   # 3:6 = 4<->6

    return list1, list2

l1, l2 = calculate(list)
print (l1, l2)
'''
print (calculate(list))
'''
print('-'*20)
    #-------------------------
# oder
print(list[0:3], list[3:6])
print('-'*20)
    #-------------------------
# oder
print(list[:3], list[3:])
print('-'*20)
    #-------------------------
# oder
list2 = [1,3,5,8,9,3]
sep_index = list2.index(8)
seperate1 = list2[:sep_index]
seperate2 = list2[sep_index:]
print(seperate1)
print(seperate2)
print('-'*20)
    #-------------------------
