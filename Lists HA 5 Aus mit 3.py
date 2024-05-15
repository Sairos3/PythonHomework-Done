'''
Aufgabe 
5. Entferne ein bestimmtes Element aus einer festgelegten Liste. 
Hinweis: Kommt ein Element mehr als einmal vor, sollte es überall entfernt werden. 
Beispiel: [3,8,9,5,1,3,6,4] ohne 3 ergibt [8,9,5,1,6,4]
'''
list = [3,8,9,5,1,3,6,4]
list2 = ['cola', 'fanta', 'pepsi', 'sprite', 'pepsi']
# nummer
no_doubles = set(list)      # set = del doubles
print(no_doubles)
# buchstaben
no_doubles2 = set(list2)
print(no_doubles2)

print('-'*50)
    #-------------------------
# oder
list = [3,8,9,5,1,3,6,4]
list.remove(3)
print(list)

print('-'*50)
    #-------------------------
# oder
list = [3,8,9,5,1,3,6,4]
while 3 in list:
    list.remove(3)
print(list)

print('-'*50)
    #-------------------------
for x in list:
    if list.count(x) > 1:
        while x in list:
            list.remove(x)
print(list)
print('-'*50)
    #-------------------------






