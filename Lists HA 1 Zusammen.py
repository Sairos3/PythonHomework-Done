'''
Aufgabe 
1. Füge zwei vorher festgelegte Listen zu einer zusammen und gib diese aus 
Beispiel: [3,8,9,2] zusammengefügt mit [4,6] ergibt [3,8,9,2,4,6] 
'''
liste1 = [3,8,9,2]
liste2 = [4,6]
zusammen = liste1 + liste2
print(zusammen)
print('1-'*20)
    #-------------------------
# oder
print(liste1 + liste2)
print('2-'*20)
    #-------------------------
# oder
liste11 = [3,8,9,2]
liste11.extend([4, 6])
print(liste11)
print('3-'*20)
    #-------------------------
# oder
liste111 = [3,8,9,2]
liste111.append(4)
liste111.append(6)
print(liste111)
print('4-'*20)
    #-------------------------
# oder
liste22 = [3,8,9,2]
liste22.insert(4, 4)
liste22.insert(5, 6)
print(liste22)
print('5-'*20)
    #-------------------------
liste12 = [3,8,9,2]
liste122 = [4, 6]
liste12.extend(liste122)
print(liste12)
print('6-'*20)
    #-------------------------
liste01 = [3, 8, 9, 2]
liste01.insert(4, 4)
liste01.insert(5, 6)
print(liste01)
print('7-'*20)
    #-------------------------
liste001 = [3,8,9,2]

liste001.insert(len(liste001), 4)
liste001.insert(len(liste001), 6)
print(liste001)
print('8-'*20)
    #-------------------------
