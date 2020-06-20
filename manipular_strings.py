#CONCATENATIG STRINGS

a = "hello"
b = a + "There"
c = a + ' ' + 'There'
print(b)
print(c)

#USING IN AS A LOGICAL OPERATOR

fruit = 'banana'
print('n' in fruit)
print('t' in fruit)
if 'a' in fruit :
    print('Found it!')

#STRING COMPARISON
word = input("enter word: ")
if word == 'banana' :
    print('Al right, bananas!')

if word < 'banana' :
    print('Your word,' + word + ',comes before banana.')
elif word > 'banana' :
    print('Your word,' + word + ',comes after banana.')
else :
    print('Al right')

#STRING FUNCTIONS IN STRING LIBRARY
# lower() object method
greet = "Hello Kify"
zap = greet.lower()
print(zap)
print(greet)
print('Hi There'.lower())

#Type method / dir method
stuff = "cats"
print(type(stuff))
print(dir(stuff)) #prints out the method of the type of data

#str.capitalize
#str.enter
#str.endswith()
#str.find()
#str.lstrip()
#str.replace()
#str.lower()
#str.rstrip()
#str.strip()
#str.upper()

#SEARCHING IN A STRING

fruta = 'pomelo'
pos = fruta.find('me')
print(pos)

aa = fruta.find('z')
print(aa)

#REPLACE
saludo = ('Hola Nina')
saludito =saludo.replace('Nina', 'Kify')
print(saludito)

 #SPACES
hello = ' Nina Danonina '

hi2 = hello.lstrip()
hi3  = hello.rstrip()
hi4 = hello.strip()

print(hi2)
print(hi3)
print(hi4)

#PREFIXES

line = 'Please, have a nice day'
print(line.startswith('Please'))
print(line.startswith('p'))

#PARSING AND EXTRACTING
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos =  data.find(' ',atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)