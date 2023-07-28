#tuples

phone_companies = ("Samsung", "iphone", "tecno", "Samsung")
print(phone_companies)

#using len on the tuple
print(len(phone_companies))#output 4

#accessing items in the tuple
print(phone_companies)
#accessing items at index 1
print(phone_companies[1])
#accessing items at index 3
print(phone_companies[3])
#accessing the second item from the back
print (phone_companies[-2])
#accessing all the items
print(phone_companies[:])
#accessing all items starting from the second one
print(phone_companies[1:])
#accessing all items to the second item
print(phone_companies[:2])



#SETS

#find the length of the set
utencils= {"plates", "forks", "spoons", "bowls", "knives"}
print(len(utencils))

#find dataType
print(type(utencils))

#access elements in the set
for x in utencils:
    print(x)
# or
print("forks" in utencils)


#adding items
utencils.add("jugs")
print(utencils)

#adding two sets together
laptops1 = {"Lenovo", "Acer", "Dell"}
laptops2 = {"HP", "Macbook"}
laptops = laptops1 | laptops2
print(laptops)