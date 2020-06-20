#Strings: type of data that gos between "".

str1 = "hello world"
name = input("Enter name: ")
print(name)

#En el siguiente ejemplo, se considera que la palabra
# banana es un arreglo de 6 letras, las cuales
#empiezan con el índice 0.

#0 b
#1 a
#2 n
#3 a
#4 n
#5 a

fruit = "banana"
letter = fruit[1] #imprime la letra con índice 1
print(letter)

x = 3
w = fruit[x - 1]
print(w) #imprimirá el índice 2 (letra n)

#A character too far = when index is out of range:

#fruit2 = "apple"
#print(fruit2[8]) 
# imprime un error "String index out of range"


#LEN FUNCTION (LENGHT FUNCTION IN JS)
#prints lenght of array
fruit3 = "pomgranate"
y = len(fruit3)
print(y)

#LOOPING TROUGH STRINGS:
fruta= "pomelo"
index = 0
while index < len(fruta) :
    a = fruta[index]
    print(index, a)
    index = index + 1

#Looping wiyh FOR: the iteration variable "iterates" through the string
#and the block (body) of code is executed once for each
# #value in the sequence 
fruta2 = "chilacayote"
for letter in fruta2 :
    print(letter) 

#SLICING STRINGS
f = "Me llamo Kify"
print(f[0:7])
print(f[6:7])
print(f[0:20])
print(f[0:1])
print(f[4:8])
print(len(f))

g = "gato en la nevera"
print(len(g))
print(g[:2])
print(g[8:])
print(g[:])