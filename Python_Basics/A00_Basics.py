"""basics of Python"""
import math

#PRINT
print("Hello, World!")

#INPUTS
name = input('What is your name? ')
print('Hi ' + name)

color = input('WHat is your favorite color? ')
print(name + ' likes ' + color)

birth_year = input('Birth year: ')
age = 2024 - int(birth_year)
print(name + ' is ' + str(age) + ' years old')

#STRINGS
course = "python course for 'beginners'"
print(course)

new = ''' 
Hi Aryan,
Hello there!

thank you,
X

''' 

print(new)

string = 'Hello there!'
print(string[0])
print(string[4])
print(string[-2])
print(string[1:7])
print(string[1:])

#formatted strings
first = 'Aryan'
last = 'Singh'
msg = f'{first} [{last}] is a coder'
print(msg)

#String Methods
print(len(msg))     # built in function

print(msg.upper())  # methods
print(msg.find('o'))
print(msg.find('O'))
print(msg.replace('coder', 'programmer'))

print('coder' in msg)
print('programmer' in msg)

#Arithmetic operations
#Operator precedence

#Math functions
x = 2.8
print(abs(x))
print(math.ceil(x))
print(math.floor(x))

#if statements && logical operators
has_good_income = True
has_good_credit = True
has_criminal_record = True

if has_good_income and has_good_credit:
    print("Eligible for loan")
else:
    print("Not Eligible for loan")

if has_good_income or has_good_credit:
    print("Eligible for loan")
else:
    print("Not Eligible for loan")

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Not Eligible for loan")

#Comparison operators
#while statement
i = 1
while i<= 5:
    print('*' * i)
    print(i)
    i += 1
print("While loop done")

#for loop
#nested loop

