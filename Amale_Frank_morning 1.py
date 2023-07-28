# using if else statements
age = 60
if (age<18):
    print('You are underage')
elif(age>=65):
    print('You are an adult')
else:
    print('You are a senior citizen')
    

# for loop
# while loop

# for i in sequence:

vehicles = ['Tesla', 'Jeep', 'Ford', 'Toyota']
for car in vehicles:
    print (car)

fruits = ['apple', 'berries', 'passion fruit', 'ovacado','orange']
for fruit in fruits:
    print(fruit)

# while loop
x = 0
while x<= 5:
    print(x)
    x += 1

fruits = ['apple', 'banana', 'watermelon', 'tomato','orange', 'pineapple']
i = 0
while i< len(fruits):
    print(fruits[i])
    i +=1
    
#break and continue
for num in range(0 ,60):
    if num == 3:
        continue
    print(num)

#exception handling
#try, except, finally:
try:
    x = 10/3
    print(x)
except:
    print("you can't devide a number by zero")
finally:
    print('Program finished')

#Exercise 1
#write a program to a student abou their mental health
#Prompt a student to rate their mental health on a scale of 1 -5
print("""
poor
moderate
good      
      """)
mental_health = input('What is your mental health on the above scale? ')

mood = {
    'poor' : "need to see a doctor",
    'moderate': 'Anything you want to share with me?',
    'good': 'Great to hear',
    
}
if mental_health.lower() in mood:
    print("you are " + mood[mental_health])
else:
    print('Please enter a value in the above range') 
