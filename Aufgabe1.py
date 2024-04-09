'''Wohnt Joe in einer größeren Stadt? False 
1.Ben Müller wohnt in einer Stadt mit 50000 Einwohnern 

2.Ben Müller wohnt in einer Stadt mit 50000 Einwohnern 
Joe Lehmann wohnt in einer Stadt mit 10000 Einwohnern 
Die beiden Städte haben zusammen 60000 Einwohner 

3.Wohnt Joe in einer größeren Stadt? False'''
# User 1
name1='Ben Müller'
einwohner1=50000

# User 2
name2='Joe Lehmann'
einwohner2=10000

#1 Ben Müller wohnt in einer Stadt mit 50000 Einwohnern 
#2 Ben Müller wohnt in einer Stadt mit 50000 Einwohnern Joe Lehmann wohnt in einer Stadt mit 10000 Einwohnern Die beiden Städte haben zusammen 60000 Einwohner 
print(name1, 'wohnt in einer Stadt mit', einwohner1, 'Einwohnern')
print(name2, 'wohnt in einer Stadt mit', einwohner2, 'Einwohner')
print('Die beiden Städte haben zusammen', einwohner1 + einwohner2, 'Einwohner')

#3 Wohnt Joe in einer größeren Stadt? False
print('Wohnt Joe in einer größeren Stadt?', einwohner1 < einwohner2)
