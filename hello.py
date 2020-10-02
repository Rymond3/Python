'''
print(type(3.5))
print(int(3.4))
print(5/2)
print(5//2)
print(2*3)
print(2**3)
pi = 3.14
print(pi)
#jaskdfñassdj
if pi % 3 < 1:
    print('')
    print(pi%3)
elif pi == 3:
    if pi < 6 and pi > 8:
        print('')
    else:
        print('a')
else:
    print('a')

a = 'mosd'
b = "kjfsdlks"
print(a + " " + b)
print(3*a)
print(len(a))
print(a[1])
print(a[1:3])
print(a[:3])

x = 1
stra = str(x)
print("me gusta", x, ".")
print("me gusta" + stra + ".")

text = input("Escribe algo...")
print(text)

i = 0
while i < 3:
    print(i)
    i = i + 1

for n in range(5):
    print(n)

print('')
for n in range(5, 10):
    print(n)

print('')
for i in range(5, 11, 2):
    print(i)

while(i >= 3):
    print('')
    break

print('a')
print('')

for letter in 'hola': #for letter in range(len(varHola)), for letter in varHola
    print(letter)  


count = 0
for letter in 'Snow!':
    print('Letter # ' + str(count) + ' is ' + str(letter))
    count += 1
    break
print(count)

print('')


#binary search for the square root
x = 25
epsilon = 0.01
high = x
low = 0
guess = (high + low) / 2.0

while abs(guess**2 - x) >= epsilon:
    if guess**2 > x:
        high = guess
    else:
        low = guess
    guess = (high + low) / 2.0
print(guess, 'se acerca a', x)


#convert int to binary
num = int(input("Escribe algo: "))
if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''
if num == 0:
    result = '0'
else:
    while num > 0:
        result = str(num % 2) + result
        num = num // 2
    if isNeg:
        result = '-' + result
print(result)


#convert float to binary
#convert float to int
num = float(input("Escribe algo: "))
counter = 0
while num % 1 != 0:
    num = num * 2
    counter += 1
num = int(num)

#convert int to binary
result = ''
if num == 0:
    result = '0'
else:
    while num > 0:
        result = str(num % 2) + result
        num = num // 2

#convert int binary to float binary
for i in range(counter - len(result)):
    result = '0' + result
result = result[:-counter] + '.' + result[-counter:]
print(result)

#En vez de comparar dos floats con x == y es mejor hacer abs(x-y) < epsilon, siendo epsilon = 0.001 o así, porque los floats suelen tener un error minúsculo


#Calculate square root by newton-rhapson
epsilon = 0.01
x = 24.0
guess = x / 2.0

while abs(guess**2 - x) >= epsilon:
    guess = guess - (((guess**2) - x) / (2*guess))
print(guess)


#function. Se puede acceder a variables exteriores, pero si se intentan modificar salta un error.
def is_even(i):
    """
    especificacion de la función
    """
    return i % 2 == 0

print(is_even(3))


#x en la definición h no es un update, es una inicialización, así que no se usa.
def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print(x)
    h()
    return x

z = g(3)
print(z)

def fact(n):
    if n == 1: 
        return 1
    else:
        return n*fact(n-1)
 

#torres de hanoi
def printMove(origen, destino):
    print(origen, '-', destino)

def towers(n, origen, destino, extra):
    if n == 1:
        printMove(origen, destino)
    else:
        towers(n-1, origen, extra, destino)
        towers(1, origen, destino, extra)
        towers(n-1, extra, destino, origen)

towers(4, 'P1', 'P2', 'P3')


#Fibonacci
def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

print(fib(3))
print(fib(4))
print(fib(5))


#Palíndromo
def isPalindrome(str):
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnñopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPalindrome(s[1:-1])
    
    return isPal(toChars(str))

print(isPalindrome(input('Escribe...')))


#Importar módulos referenciándolos
import circle
pi = 3
print(pi)
print(circle.pi)
print(circle.area(3))
print(circle.circumference(3))

#Importar módulos sin referenciarlos
from circle import *
print(pi)
print(area(3))


#File handler
#writeHandle es el handle que va a guardar en el archivo fileName
writeHandle = open('fileName.txt', 'w')
for i in range(2):
    name = input('Enter name: ')
    writeHandle.write(name + '\n')
writeHandle.close()

#readHandle es el handle que va a leer del arcchivo fileName
readHandle = open('fileName.txt', 'r')
for line in readHandle:
    print(line)
readHandle.close()


#tuples: ordered sequence of immutable elements, can mix different types
te = ()
t = (2, 'one', 3)
t[0] #devuelve 2
t + (5, 6) #devuelve (2, 'one', 3, 5, 6)
t[1:2] #devuelve ('one',), si no hubiese coma no sería tuple: 'one'
t[1:3] #devuelve ('one', 3)
t[1] = 4 #error, no se puedde modificar 

#allow to swap values (x, y) = (y, x)
mylist = [('foo','bar'),('foo1','bar1'),('foofoo','barbar')]
swapped = [(t[1], t[0]) for t in mylist] #devuelve [('bar','foo'),('bar1','foo1'),('barbar','foofoo')]

#allow to return more than one variable
def funcion():
    x = 1
    y = 2
    return (x, y)

(x, y) = funcion()


#list: ordered sequence of mutable elements, can contained types, but is not common
l1 = []
l2 = [2, 'a', 4, True]
l = [2, 1, 3]
len(l)
l[0]
l[2] = 5

total = 0
for i in L:
    total += i


l = [2, 1, 3]
l.append(5) #l = [2, 1, 3, 5]

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2 #l3 = [1, 2, 3, 4, 5, 6]
l1.extend([0, 6]) #l1 = [1, 2, 3, 0, 6]
del(l1[3]) #l1 = [1, 2, 3, 6]
l1.pop() #l1 = [1, 2, 3]

l = [1, 2, 5, 2]
l.remove(2) #l = [1, 5, 2]
l.remove(3) #error


s = 'hola amigo'
list(s) #devuelve el string en formato list ['h', 'o', ...]
s.split(' ') #devuelve la lista separada por ese caracter ['hola', 'amigo']

l = ['a', 'b', 'c']
''.join(l) #convierte la lista en string 'abc'
'_'.join(l) #convierte la lista en string insertando el caracter entre los elementos 'a_b_c'

l = [9, 6, 0, 3]
sorted(l) #devuelve la lista ordenada, también con strings
l.sort() #ordena la lista, también con strings
l.reverse() #ordena la lista en orden descendente 

#range(5) es equivalente a (0, 1, 2, 3, 4)
#range(5, 2, -1) es equivalente a (5, 4, 3)


#las listas son punteros
a = [1, 2, 3]
b = a
b[1] = 5 #a[1] = 5

a = [1, 2,3]
b = a[:] #se hace una copia de a a b, pero no apuntan a lo mismo


def removeDuplicates(l1, l2):
    for e in l1:
        if e in l2:
            l1.remove(e)

l1 = [1, 2, 3, 4]
l2 = [1, 2, 5, 6]
removeDuplicates(l1, l2)
#problema: el for funciona con un contador, así que al eliminar el 1 el 2 se convierte en el elemento 0, lo que implica que no se itera el 2
#solución:

def removeDuplicates(l1, l2):
    l1copy = l1[:]
    for e in l1copy:
        if e in l2:
            l1.remove(e)


def applyToEach(list, function):
    for i in range(len(list)):
        list[i] = function(list[i])

l = [1, -2, 3.4]
applyToEach(l, abs)
print(l)
applyToEach(l, int)
print(l)


def applyFuns(l, x):
    for f in l:
        print(f(x))

applyFuns([abs, int], -3.4)


#map takes a function and as many collections as arguments and applies that function to all the elements of the collections
#produces an iterable, so we need to iterate it
for elt in map(abs, [1, -2, 3, -4]):
    print(elt)

l1 = [1, 28, 33]
l2 = [2, 57, 9]
for elt in map(min, l1, l2):
    print(elt)


#seq can be a string, tuple, range or list. Common operations:
seq[i] #ith element of the sequence
len(seq) #length of the sequence
seq1 + seq2 #concatenation of sequences (not range)
n*seq #sequence that repeats seq n times (not range)
seq[start:end] #slice of the sequence
e in seq #True if e contained in seq
e not in seq #true if e not contained in seq
for e in seq #iterates over all elements of seq


#diccionarios. Neither keys nor values are ordered. Keys must be unique and have an immutable type (int, float (not recommended), string, tuple or bool)
dic = {}
grades = {'Ana': 'B', 'Jhon': 'C'}
grades['John'] #Evaluates to 'C'
grades['Daisy'] #Evaluates to KeryError
grades['Daisy'] = 'B+' #Adds the entry 'Daisy': 'B+'
'Daisy' in grades #True if Daisy in grades
del(grades['Daisy']) #Deletes the entry of Daisy
grades.keys() #Gives an iterable of all the keys
grades.values() #Gives an iterable of all the values


#ejemplo diccionario
def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)

def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
    return result


#fib diccionario
def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans


#Global variables for tracking efficiency
numFibCalls = 0

def fib(n):
    global numFibCalls
    numFibCalls += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)

print(fib(12))
print(numFibCalls)

        
#Exceptions
try:
    a = 3
    #a = 'asd'
    b = 0
    #b = 2
    print('a/b = ', a/b)
    print('a+b = ', a+b)
except ValueError:
    print('Could not convert to a number')
except ZeroDivisionError:
    print("Can't divide by zero")
except:
    print('Something went wrong')
else:
    print('Everything went fine')
finally: #Siempre se ejecuta
    print('End')


while True:
    try:
        n = input('Enter an integer: ')
        n = int(n)
        break
    except ValueError:
        print('Not an integer... Try again')
print(n, 'is an integer')


data = []
file_name = 'fileName.txt'

try:
    fh = open(file_name, 'r')
except IOError:
    print('Cannot open', file_name)
else:
    for line in fh:
        if line != '\n':
            addIt = line[:1].split(',') #Remove endline \n
            data.append(addIt)
finally:
    fh.close()


raise ValueError('Something went wrong')

data = []
assert not len(data) == 0, 'no data' #Throws assert exception with that description


#clases. Recomendado hacer getters y setters
class Coordinate(object): #object es la clase padre
    tag = 1 #Variable global compartida entre todas las instancias de Coorinate
    def __init__(self, x, y):
        #A.__init__(self...) si la clase hereda de la clase A
        self.x = x
        self.y = y
    def distance(self, other):
        x_diff = (self.x - other.x)**2
        y_diff = (self.y - other.y)**2
        return (x_diff + y_diff)**0.5
    def __str__(self): 
        return '<' + str(self.x) + ', ' + str(self.y) + '>'
    #__add__ __sub__ __eq__ __lt__ __len__ overloads de operadores

origin = Coordinate(3, 4)
print(origin.x)
print(origin) #__str__
print(isinstance(origin, Coordinate)) #True


class HomeCoordinate(Coordinate):
    pass #La clase no contiene nada



#Generadores
def genTest():
    yield 1 #Para la ejecución y devuelve el valor
    yield 2

foo = genTest()
#next() comienza o continúa la ejecución del procedimiento. Ejecuta hasta alcanzar a un yield.
foo.__next__() #Devuelve 1 
foo.__next__() #Devuelve 2
foo.__next__() #Levanta una StopIteration exception

for n in genTest():
    print(n) #Ejecuta todos los yields: 1 \n 2


def genFib():
    fibn_1 = 1
    fibn_2 = 0
    while True:
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next

for n in genFib():
    print(n)
'''


import pylab as plt


mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)

plt.plot(mySamples, myLinear)
























