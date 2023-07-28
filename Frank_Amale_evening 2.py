#Ecercise one lists
print('**********************************')
print('exercise 1')
print('**********************************')


#1
names = ['Junior', 'martha', 'Daphne', 'James', 'John']
print (names[1])

#2
names[0] = 'Jane'
print (names)

#3
names.append('Mary')
print (names)


#4
names.insert(2, 'Bethel')
print (names)

#5
names.remove(names[2])
print (names)

#6
print(names[-1])

#7

colors = ['yellow', 'green', 'blue', 'indigo', 'orange', 'white', 'grey']
print (colors[2:5])

#8
countries = ['Uganda', 'Canada', 'United States', 'kenya', 'Rwawnda', 'Tanzania', 'Argentina']
countries_copy = countries[:]

#9
for country in countries:
    print(country)

#10
animals = ['cat','dog', 'goat', 'cow', 'sheep']
animals.sort()
print (animals)

animals.sort(reverse=True)
print (animals)

#11
for animal in animals:
    if 'a' in animal:
        print (animal)

#12
fnames =['Jackie', 'Amos', 'Adam', 'Julius']
snames =['Ssekitto', 'Ssebandeke', 'Kato', 'Saava']

names = fnames + snames
print(names)


#Exercise 2 tuples
print('**********************************')
print('exercise 2')
print('**********************************')
#1
x = ('sumsung', 'iphone', 'tecno', 'redmi')
print(x[0])

#2
print(x[-2])

#3
y = list (x)
y[1] = 'itel'
x = tuple(y)
print(x)

#4
y = list (x)
y.append('Huawei')
x = tuple(y)
print(x)

#5
for item in x:
    print(item)

#6
y = list (x)
y.remove('tecno')
x = tuple(y)
print(x)

#7
cities = tuple(['Kampala', 'Jinja', 'Massaka', 'Gulu', 'Arua'])
print(cities)

#8
a, b, c, d, e = cities
print(a)
print(b)
print(c)
print(d)
print(e)
    
#9
print(cities[2:5])

#10
fnames =('Jackie', 'Amos', 'Adam', 'Julius')
snames =('Ssekitto', 'Ssebandeke', 'Kato', 'Saava')
fullnane = fnames + snames
print(fullnane)

#11
colors = ['yellow', 'green', 'blue', 'indigo', 'orange', 'white', 'grey']
newColors = colors *3
print (newColors)

#12
thistuple = (1,3,7,8,7,5,4,6,8,5)
print(thistuple.count(8))

#exercise 3 Sets
print('**********************************')
print('exercise 3')
print('**********************************')

#1
beverages = set(['tea','coffee','Juice']) 

#2
beverages.add('Soyacup')
beverages.add( 'Ginger')
print(beverages)

#3
myset = {'oven', 'kettle', 'microwave', 'refridgelator' }

if 'microwave' in myset:
    print("microwave present")
    
#4
myset.remove('kettle')
print(myset)

#5
for item in myset:
    print(item)

#6
set1 = {'cups', 'plates', 'spoons', 'forks'}
list1 = ['dishes', 'bowls']

st = set(list1)

print (set1.union(st))

#7
names = {'Amale', 'Frank', 'Junior'}
ages = {20, 21, 22}

combination = names.union(ages)
print (combination)

#Exercise4 Strings
print('**********************************')
print('exercise 4')
print('**********************************')
#1
name ='amale frank'
age = 21
print(name + ' '+str(age))

#2
txt = '       HEllo, Uganda!    '
txt = txt.strip()
print(txt)

#3

print(txt.upper())

#4
tex = txt.replace('U', 'V')
print(tex)

#5
y = 'I am proudly ugandan'
print(y[2:5])

#6
x = 'All "Data Scientists" are cool'

#Exercise 5 (Dictionaries)
print('**********************************')
print('exercise 5')
print('**********************************')
#1
shoes = {
    'Brand' : 'Nick',
    'color' : 'black',
    'size' : 40
}
print(shoes['size'])

#2
shoes['Brand'] = 'Adidas'
print(shoes)

#3
shoes['type'] = 'Sneakers'
print(shoes)

#4
print(shoes.keys())


#5
print(shoes.values())

#6
if 'size' in shoes:
    print("Size is in dictionary")
    
#7
for item in shoes:
    print(shoes[item])
    
#8
shoes.pop('color')
print(shoes)

#9
shoes.clear()

#10
marks = {
    'frank' : 80,
    'junior' : 62,
    'Jesca' : 85,
}

copy_marks = marks.copy()

print(copy_marks)

#11
myFamily ={
    'FirstChild' :{
        'name' : 'Amale Frank',
        'age' : 26
    },
    'secondaryChild' :{
        'name' : 'Nannyombi Jesca',
        'age' : 23
    },
    'thirdChild' :{
        'name' : 'Lule Victor',
        'age' : 18
    }
}
print(myFamily)
