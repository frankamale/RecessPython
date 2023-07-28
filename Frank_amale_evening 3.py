# functions
# from math import sqrt, factorial
# import Frank_amale_evening


# def afternoon(fname, lname):
#     print('Class starts at 2ps')
#     print('Attendees are close to 100')
#     print(f'Your name is {lname} {fname}')


# calling a function
# afternoon("William", 'Luzze')


# modules
# def add(s, w):
#     return (w+s)


# def multiply(s, w):
#     return (w*s)


# print(Frank_amale_evening.add(23, 4))

# importing squreroot and factorial from math


# print(sqrt(16))
# print(factorial(3))


# input and output in python

# name = input('Enter yourname: ')
# print('Hi '+name)


# number = int(input('enter number: '))
# product = number*45
# print(product)

# s, r, w = map(int, input('Enterthe numbers: ').split())
# print('The values are: ', end=' ')

# print(s, r, w)

# Capture input from a tuple
w = (2, 5, 3, 4, 5, 9)
print('current tuple')
print(w)

e = list(w)
e.append(int(input('Enter new value: ')))

w = tuple(e)
print('updaed_tuple ')
print(w)
