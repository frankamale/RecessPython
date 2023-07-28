# Exception handling

# Using finally and else in exception handling

import os
numb1 = int(input('enter first number: '))
numb2 = int(input('enter second number: '))
try:
    sum = numb1/numb2
except Exception:
    print('An error occurred')
else:
    print('Everything looks good')
finally:
    print('this is always executed')

# devided by 0
x = int(input('Number 1: '))
y = int(input('Number: '))


def divide(x, y):
    return x / y


try:
    print(divide(x, y))

except ZeroDivisionError:
    print('Cannot divide by zero')


# index error for index out of range
fruits = ['orange', 'melon', 'berry']
try:
    print(fruits[1])
    print(fruits[3])
except IndexError:
    print('index out of range')


# type error
numbber = 43
number1 = 'i am fine'
try:
    z = numbber + number1
except TypeError:
    print('cannot add an integer to a string')


# KeyError
ages = {
    'Dana': 21,
    'Martha': 22,
    'Jude': 23
}
try:
    marks = ages['Junior']
    print(marks)
except KeyError:
    print("Could not find key in dictionary")


# name error
try:
    print(t)
except:
    print('parameter not defined')


##########################################################################
# File Handlling
# we use open to create a file
# it takes two parameters wc include
# -the file name and mode
# r- opens for reading and returns an error if file does not exist
# a - opens file for appending and creates one if it does not exist
# w - opens file for writing and creates one if it does not exist
# x - creates a specified file and returns an error if it already exists

# open a file
# file1 = open('jun.txt', 'x')


# write to a file
fw = open('jun..txt', 'w')
fw.write('Hello World \n')
fw.write('Am on the second line in the file\n')


# closing the file
fw.close()

# read from a file
f = open('jun.txt', 'r')
print(f.read())

f.close()

# appending to the file

app = open('jun.txt', 'a')
app.write('\n i have appended this\n')

app.close()

# read contents again
readf = open('jun.txt', 'r')
print(readf.read())

readf.close()

# deleting a file

# os.remove('jun.txt')
