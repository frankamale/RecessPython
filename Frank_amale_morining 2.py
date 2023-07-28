

# #day 3

# #basic operators and Expressions (input and output)
# # - Arithmetic operators
# # + Addition
# # - Subtraction
# # * multiplication
# # / division
# # // devide witout remainder
# # % moduluus
# # ** exponential

# # comparison operators
# #  == equal to
# #  != not equal to
# # > greater than 
# # < less than
# # >= greater than or equal to
# #  <= less than or equal to


# # Logical operators
# # logical AND 'and' 
# # logical OR 'or'
# # logical NOT 'not'


# # - Assignment operators
# # Asssign a value: '='
# # add value: '+'
# # Add and assign a value: '+='
# # Subtract and asssign a value: '-='

# # -Membership operators
# #  In : 'in' operator: checks if a value exists in a sequence
# # not in: not in operator: checks if a value does not exist in a sequence

# # - Identity operators
# # Is: 'is' Checks if two values are the same
# # Is not: 'is not' operator: checks if two values are not the same

# # Examples

# # + Addition
# x = 50  + 45
# print(x)
# # - Subtraction
# y = 50  - 45
# print(y)
# # * multiplication
# z = 50  * 45
# print(z)
# # / division
# m = 50  / 45
# print(m)
# # // devide witout remainder
# x = 50  // 45
# print(x)
# # % moduluus
# z = 50  % 45
# print(z)
# # ** exponential
# q = 50  ** 45
# print(q)

# # comparison operators
# x = 10
# y = 9
# #  == equal to
# if x == y:
#     print("a is equal to b")
#     print (x==y)
# #  != not equal to
# if x != y:
#     print("a is not equal to b")
#     print (x!=y)
# # > greater than 
# if x >y:
#     print("a is greater than b")
#     print (x>y)
# # < less than
# if x < y:
#     print("a is less than b")
#     print (x<y)
# # >= greater than or equal to
# if x >= y:
#     print("a is greater than or equal to b")
#     print (x>=y)
# #  <= less than or equal to
# if x <= y:
#     print("a is less than or equal to b")
#     print (x<=y)
    
# print(x < y)

# x = True
# y = False
# # logical AND 'and' 
# print (x and y)
# # logical OR 'or'
# print (x or y)
# # logical NOT 'not'
# print(not x)
# print(not y)

# # compound assigment operators

# x = 70
# # add and assign
# x +=40
# print (x)

# #subtract and assign
# y = 100
# y -= 17
# print (y)

# # Divie and asssign a value: '/='

# z = 150
# z /= 3
# print (z)
# # Modulus and assign a value: %=

# p = 72
# p %= 5
# print (p)
# # exponantiate and assign a value: *=

# q = 5
# q *= 2
# print (q)

# # -Membership operators
# cars = ['BMW', 'Audi', 'Jeep', 'Rolls Royce']
# #  In : 'in' operator: checks if a value exists in a sequence
# if 'Jeep' in cars:
#     print('Jeep is in the list')
# else:
#     print('Jeep is not in the list')
# # not in: not in operator: checks if a value does not exist in a sequence
# if 'Toyota' not in cars:
#     print('Toyota is not in the list')
# else:
#     print('Toyota is in the list')
    

# # identity operators
# x = 10
# y = 10
# print (x is y)
# print (x is not y)

# list = range(1, 10)
# list2 = range(1, 10)

# print(list is  list2)
# print(list is not list2)

# #Bitwise operator
# # are use to make operations on individual bits in binary numbers
# # bitwise AND '&' and Bitwise OR '|' operator
# # btwise XOR '^' 
# # Bitwise NOT '-' 
# # bitwise left shift '<<'
# # bitwise right shift '>>'


# # Examples of bitwise operations
# a = 10
# b = 20

# # bitwise AND '&' 
# print (a&b)

# # Bitwise OR '|' operator
# print (a|b)
# # btwise XOR '^' 
# print (a^b)
# # Bitwise NOT '-' 
# print(-a)
# # bitwise left shift '<<'
# print (a<<b)
# # bitwise right shift '>>
# print (a>>b)

# # create a simple calculattor to add, subtract, multiply, and devide
# def add(a, b):
#     return a + b
# def subtract(a, b):
#     return a - b
# def multiply(a, b):
#     return a * b
# def divide(a, b):
#     return a / b

# def main():
#     print ('My first calculator')
#     number1 = float(input('Enter first number: '))
#     number2 =float( input('Enter second number: '))
#     operator = input("operator ('+, -, *, /) : ")
    
#     if operator == '+':
#         result = add(number1, number2)
#     elif operator == '-':
#         result = subtract(number1, number2)
#     elif operator == '*':
#         result = multiply(number1, number2)
#     elif operator == '/':
#         result = divide(number1, number2)
#     else:
#         print('Invalid operator')
    
#     print ('the result is ', result)
    
# if __name__ == '__main__':
#     main()
    
    
#     #Assignmet 1: Create a simple calsculator program with a GUI.
#     # Make the title of your calcutor program window with your name eg frank Junior Simple calculator

import tkinter as tk

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    expression = display.get()
    try:
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except Exception:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Create the window
window = tk.Tk()
window.title("Amale Frank Simple Calculator")

# Create the display
display = tk.Entry(window, width=50, justify=tk.RIGHT)
display.grid(row=0, column=0, columnspan=4)

# Create number buttons
for i in range(1, 10):
    button = tk.Button(window, text=str(i), padx=20, pady=5, command=lambda num=i: button_click(num))
    button.grid(row=(9-i)//3 + 1, column=(i-1)%3)

# Create other buttons
button_0 = tk.Button(window, text="0", padx=20, pady=5, command=lambda: button_click(0))
button_0.grid(row=4, column=0)
button_clear = tk.Button(window, text="C", padx=20, pady=5, command=button_clear)
button_clear.grid(row=4, column=1)
button_equal = tk.Button(window, text="=", padx=20, pady=5, command=button_equal)
button_equal.grid(row=4, column=2)
button_add = tk.Button(window, text="+", padx=20, pady=5, command=lambda: button_click("+"))
button_add.grid(row=3, column=3)
button_subtract = tk.Button(window, text="-", padx=20, pady=5, command=lambda: button_click("-"))
button_subtract.grid(row=2, column=3)
button_multiply = tk.Button(window, text="*", padx=20, pady=5, command=lambda: button_click("*"))
button_multiply.grid(row=1, column=3)
button_divide = tk.Button(window, text="/", padx=20, pady=5, command=lambda: button_click("/"))
button_divide.grid(row=4, column=3)

# Run the main loop
window.mainloop()
