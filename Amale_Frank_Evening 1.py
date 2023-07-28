#dictionaries
#they are changeable bt dont allow duplicates
#one dictionary can have different data items with differnt datatypes


mydict = {
    'phone' : 'iphone',
    'iphoneModel' : 'iphone 14',
    'year' : 2023
}
print (mydict)
print (len(mydict))
print (type(mydict))

#Access dictionary items
print (type((mydict['phone']))) 

year = mydict['year']
print(year)

iphoneModel = mydict.get('iphoneModel', 'no model here')
print(iphoneModel)

w = mydict.keys()
print(w)
#Exercise 1; use values method to retrieve to return the list of all values in the dictionary
colors = {
     1 : 'Blue',
    2 : 'red',
    3 : 'orange',
    4 : 'black'
}
print (colors.values())
#Exercise 2: to check if a key exists in the dictionary
colors = {
     1 : 'Blue',
    2 : 'red',
    3 : 'orange',
    4 : 'black'
}
if 1 in colors:
    print('key exists in dictionary')

#exercise 3; Give an example on how to change dictionary items, update the dictionary
colors = {
    1 : 'Blue',
    2 : 'red',
    3 : 'orange',
    4 : 'black'
}
colors[1] =  "form one"
print(colors[1])

#Exercise 4; An example on how to add dictionary items, how to remove dictionary items
colors = {
     1 : 'Blue',
    2 : 'red',
    3 : 'orange',
    4 : 'black'
}
colors[5] = 'yellow'
colors[6] = 'green'
print(colors.values())

#removing dictionary items
colors.pop(1)
colors.pop(2)
print(colors.values())

#exercise 5; An example on how to loop through a dictionary and how to nest dictionaries
colors = {
     1 : 'Blue',
    2 : 'red',
    3 : 'orange',
    4 : 'black'
}
for x in colors:
    print (colors[x])
    
    
# numbers
#integers, floats complex

w = 10
e = 12.43
z = 4j
print(type(w))
print(type(e))
print(type(z))

#integers
a = 1232113
b = 2
c = -23422

print(type(a))
print(type(b))
print(type(c))

#complex
w = 6 +10j
t = -4j
h = 2j
print(type(w))
print(type(t))
print(type(h))


no = 30
z = complex(no)
print(type(z))

#conver from int to float
#convert float to complex

length = 300
leng = float(length)
print(type(leng))

height = 6.4
hei = complex(height)
print(type(hei))

#Casting
#used to specify a variabl type

h = int(20)
y = int(3000)
a = int("2")
print(h)
print(y)
print(a)

#Strings
#both double and single quotes work
print('Afternoon')
print("Afternoon")

#Assigning a string
w = "Afternoon"
print(w)

#multiline strings
#here we usw three quotes
q = '''i am in BSSE year 3
Currrently doing recess in python,
Data science,
Django
'''
print (q)

#strings as arrays

a= 'Afternoon'
print (a[5])

#Exercise 1: Use the len function to determine the length your string
month = "January"
print (len(month))

#Exercise 2: use a for loop on in a string
words = 'I am a BSSE student'
for x in words:
    print (x)

#Exercixe 3:Give an example of slicing in strings
hobbies =  'i like movies'
print(hobbies[2:7])

#How to modify strings using differnt methods in python
a = 'Afternoon'
print(a.lower())
print(a.upper())

b = '   Afternoon      '
print(b.split())

#concatenation of strings
c = 'Afternoon'
d = 'Class '
w = c + d
print(w)

z = c + " " +d
print(z) 


#Format strings
#is used when one is combining a string to a number

age = 23
name = 'My name is Frank, I am '
print(f"{name} {age}")

#booleans TRue of False
print(20<10)
print (30==40)
print (30>10)

print (bool(15))

r = 'Frank'
z = 22

print (bool(r))
print (bool(z))

# Exercise Use conditional statement to show how to use boolean
count = 0
while (count < 100):
    if (count%2 !=0):
        print (count)
    count += 1
