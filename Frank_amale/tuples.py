#store items in a single list
#are ordered and unchangeable

phones = ("Samsung", "iphone", "tecno", "Samsung")
print(phones)

#using len on the tuple
print(len(phones))#output 4


print(phones)

print(phones[1])

print(phones[3])

print (phones[-2])

print(phones[:])

print(phones[1:])

print(phones[:2])


#adding two tuples
fruit = ("oranges", "lemons", "aples")
more_fruits = ("banana", "pineapple", "watermelon")

fruit += more_fruits
print(fruit)
#using a for loop to print a tuple
for y in phones:
    print(y)

