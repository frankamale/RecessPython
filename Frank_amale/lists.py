#declaring a list
employees = ['Amale', "Kisakye", "JUlius", "Hope"]
print (employees)

employees = ['Amale', "Kisakye", "JUlius", "Hope", "martha"]
print(employees)
#length
print(len(employees))
#type
print (type(employees))

#accessing the items items
print(employees[2])
print (employees[-2])
print (employees[-5])

employees[1] = 'omaley'
print(employees)

#add an item at the end
employees.append('Jane')
print(employees)

print(employees[2:5])
print(employees[:])

print(employees[:3])

print(employees[2:])

employees.insert(3, 'James')
print(employees)
#removing an item
employees.remove("martha")
print(employees)
#removing an item using an index
employees.pop(3)
print(employees)
