# # INHERITANCE

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f'{self.name} is eating')


# class Cat(Animal):
#     def meow(self):
#         print('meeoow')


# class Dog(Animal):
#     def bark(self):
#         print('barking...')


# animal = Animal('big animal')
# cat = Cat('mart')
# dog = Dog('Sam')

# animal.eat()
# cat.eat()
# dog.eat()
# dog.bark()

# # example 2


# class Vehicle:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

#     def display_info(self):
#         print('Brand:', self.brand)
#         print('Color:', self.color)


# class Car(Vehicle):
#     def __init__(self, brand, color, num_wheels):
#         super().__init__(brand, color)
#         self.num_wheels = num_wheels

#     def honk(self):
#         print('Honking the horn..')


# car1 = Car('Toyota', 'black', 4)
# car1.color = 'red'
# car1.display_info()


# # exercise 1
# # use inheritance to calculate area and perimeter of a circle and rectangle

# class Shape:
#     def __init__(self, area, perimeter):
#         self.area = area
#         self.perimeter = perimeter

#     def display(self):
#         print(f"the area is {self.area} ")
#         print(f"the perimeter is {self.perimeter}")


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#         # self.area /= area

#     def calculteArea(self):
#         self.area = 3.14 * self.radius ** 2

#     def calculatePerimeter(self):
#         self.perimeter = 2 * 3.14 * self.radius


# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def calculteArea(self):
#         self.area = self.length * self.width

#     def calculatePerimeter(self):
#         self.perimeter = (2*self.length) + (2 * self.width)


# c1 = Circle(7)
# c1.calculatePerimeter()
# c1.calculteArea()
# c1.display()

# r1 = Rectangle(4, 3)
# r1.calculatePerimeter()
# r1.calculteArea()
# r1.display()

# # Example3
# # Multiple inheritance


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f'{self.name} is eating')


# class Flyable:
#     def fly(self):
#         print(f'{self.name} is flying')


# class Bird(Animal, Flyable):
#     def __init__(self, name, species):
#         self.species = species
#         self.name = name

#     def display_info(self):
#         print(f'Species: {self.species}')
#         print(f'Name: {self.name}')


# my_bird = Bird('pigeon', 'bird')


# my_bird.eat()
# my_bird.fly()


# # Method overidding
# class Animal:
#     def make_sound(self):
#         print('Animal is making sound')


# class Cat(Animal):
#     def make_sound(self):
#         print('Cat is meowing...')


# class Dog(Animal):
#     def make_sound(self):
#         print('Dog is barking...')


# def make_animal_sound(animal):
#     animal.make_sound()


# cat = Cat()
# dog = Dog()
# animal = Animal()

# make_animal_sound(cat)
# make_animal_sound(dog)
# make_animal_sound(animal)


# polymorphism
# writing code that can run with different objects

# Method overriding
# method overloading


# from abc import ABC, abstractmethod


# class Shape:
#     def calculate_area(self):
#         return self.length * self.width


# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def calculate_area(self):
#         return 3.14 * self.radius ** 2

#     def calculate_circumference(self):
#         return 2 * 3.14 * self.radius


# rectangle = Rectangle(4, 6)
# circle = Circle(14)

# print('area of rectangle', rectangle.calculate_area())
# print('area of circle', circle.calculate_area())
# print('Circumference of circle', circle.calculate_circumference())


# Abstraction
# from abc import ABC, abstractmethod


# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass


# class Car(Vehicle):
#     def start(self):
#         print('Starting the car...')

#     def stop(self):
#         print('Stopping the car...')


# class Truck(Vehicle):
#     def start(self):
#         print('Starting the truck...')

#     def stop(self):
#         print('Stopping the truck...')


# car = Car()
# truck = Truck()

# car.start()
# car.stop()

# truck.start()
# truck.stop()

# Exercise 2
# demostrate abstraction calculating area of a circle and rectangle

# from abc import ABC, abstractmethod


# class Shape(ABC):
#     @abstractmethod
#     def calculate_area(self):
#         pass

#     @abstractmethod
#     def display(self):
#         pass


# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def calculate_area(self):
#         self.area = self.length*self.width

#     def display(self):
#         print(f'area is {self.area}')


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def calculate_area(self):
#         self.area = 3.14 * self.radius ** 2

#     def calculate_circumference(self):
#         self.circumference = 2 * 3.14 * self.radius

#     def display(self):
#         print(f'area is {self.area}')
#         print(f'circumference is {self.circumference}')


# rectangle = Rectangle(4, 6)
# circle = Circle(14)
# circle.calculate_area()
# circle.calculate_circumference()
# circle.display()

# rectangle.calculate_area()
# rectangle.display()


# assignment
# create a receipt printing program using GUI interface
from tkinter import *


class Receipt:
    def __init__(self, master):
        self.master = master
        self.master.title("Frank's Grocery Receipt System")
        self.master.geometry("500x500")
        self.master.config(bg="#f2f2f2")

        # Create Labels
        self.lbl_item = Label(self.master, text="Item Name",
                              font=("Arial", 12), bg="#f2f2f2")
        self.lbl_item.grid(row=0, column=0, padx=10, pady=5)

        self.lbl_price = Label(self.master, text="Price",
                               font=("Arial", 12), bg="#f2f2f2")
        self.lbl_price.grid(row=0, column=1, padx=10, pady=5)

        # Create Entries
        self.ent_item = Entry(self.master, font=("Arial", 12), width=20)
        self.ent_item.grid(row=1, column=0, padx=10, pady=5)

        self.ent_price = Entry(self.master, font=("Arial", 12), width=10)
        self.ent_price.grid(row=1, column=1, padx=10, pady=5)

        # Create Listbox with Scrollbar
        self.lb_items = Listbox(self.master, font=(
            "Arial", 12), width=30, height=5)
        self.lb_items.grid(row=2, columnspan=2, padx=10, pady=5)
        self.scrollbar_lb = Scrollbar(self.master, command=self.lb_items.yview)
        self.scrollbar_lb.grid(row=2, column=2, sticky='ns')
        self.lb_items.config(yscrollcommand=self.scrollbar_lb.set)

        # Create Buttons
        self.btn_add = Button(self.master, text="Add Item", font=(
            "Arial", 12), command=self.add_item)
        self.btn_add.grid(row=3, columnspan=2, padx=10, pady=10)

        self.btn_print = Button(self.master, text="Print Receipt", font=(
            "Arial", 12), command=self.print_receipt)
        self.btn_print.grid(row=4, columnspan=2, padx=10, pady=10)

        # Create Total Label
        self.lbl_total = Label(self.master, text="",
                               font=("Arial", 12), bg="#f2f2f2")
        self.lbl_total.grid(row=5, columnspan=2, padx=10, pady=5)

        # Create Receipt Display with Scrollbar
        self.receipt_display = Text(
            self.master, font=("Arial", 12), width=40, height=8)
        self.receipt_display.grid(row=6, columnspan=2, padx=10, pady=5)
        self.scrollbar_rd = Scrollbar(
            self.master, command=self.receipt_display.yview)
        self.scrollbar_rd.grid(row=6, column=2, sticky='ns')
        self.receipt_display.config(yscrollcommand=self.scrollbar_rd.set)

    def add_item(self):
        item = self.ent_item.get()
        price = float(self.ent_price.get())
        item_price = f"{item} - shs.{price:.2f}"
        self.lb_items.insert(END, item_price)

        # Clear Entries
        self.ent_item.delete(0, END)
        self.ent_price.delete(0, END)

    def print_receipt(self):
        self.receipt_display.delete(1.0, END)
        total_cost = 0.0
        self.receipt_display.insert(END, "Receipt:\n\n")
        for i in range(self.lb_items.size()):
            item_price = self.lb_items.get(i)
            item_name = item_price.split(" - ")[0]
            price = float(item_price.split(" - ")[1].replace("shs.", ""))
            total_cost += price
            self.receipt_display.insert(
                END, f"{i + 1}. {item_name}: shs.{price:.2f}\n")
        self.receipt_display.insert(END, f"\nTotal: shs.{total_cost:.2f}")


root = Tk()
app = Receipt(root)
root.mainloop()
