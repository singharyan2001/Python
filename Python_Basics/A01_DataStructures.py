"""Data structures - lists, tuples, dictionary, classes"""

#lists
names = ['Aryan', 'Hussain', 'Aman', 'Ishaan', 'Tejas']
print(names)
print(names[0])
print(names[4])
print(names[-3])
print(names[-2])
print(names[3:])
print(names[1:3])
print(names[:4])

#write a program to find the largest number in a list
listValues = [1,2,3,4,5,6,7,8,9,0]
max = listValues[0]
for listValues in listValues:
    if listValues > max:
        max = listValues
print('max value is : ' + str(max))

#2D Lists
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[0][0])
print(matrix[2][1])

for row in matrix:
    for item in row:
        print(item)

#List Methods
numbers = [5,2,1,7,4]

numbers.append(11)          #We can append/attach a number at the end of a list
print(numbers)

numbers.insert(0, -1)       #We can insert elements at any location in the list and the elements would shift right.
print(numbers)

numbers.remove(7)           #we can remove an element [specify value] in the list.
print(numbers)

numbers.pop()               #we will remove/pop a the last element in the list.
print(numbers)

print(numbers.index(-1))    #checks for the existence of an item in our list.

print(4 in numbers)         #Using the "in operator"

numbers.sort()              #we can sort the list in place.[Ascending order]
print(numbers)

old_numbers = numbers.copy()

numbers.reverse()           #we can reverse the list.
print(numbers)

new_numbers = numbers.copy()

numbers.clear()             #clears the entire list
print(numbers)

new_numbers.append(10)
print(new_numbers)

old_numbers.append(7)
print(old_numbers)

'''Write a program to remove the duplicates in a list'''
new_list = [5,3,4,6,6,8,1,9,3,7]
print(new_list)
unique_list = []

for i in new_list:
    if i not  in unique_list:
        unique_list.append(i)

print(unique_list)


#Tuples
xyy = (9,7,11)
print(xyy)
print(xyy[1])

#unpacking

coordinates = (1,2,3)
'''
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
This method not recommended, not efficient
'''
#this is much more efficient ; #can also use this with lists as well.
x,y,z = coordinates
print(x)
print(y)
print(z)

#Dictionaries - key:value pairs
Employee = {
    'Name': "Aryan Singh",
    'Age' : 23,
    'DOB' : "14.03.24",
    'Designation' : "Embedded Systems Engineer",
    'Company': "Nxtqube",
    'is_Alive': True
}

print(Employee['Name'])
print(Employee['Age'])
print(Employee['DOB'])
print(Employee['Designation'])
print(Employee['Company'])
print(Employee['is_Alive'])

print(Employee.get('name'))         #gets the value for the key specified, if not found returns None
print(Employee.get('Age')) 

Employee['CGPA'] = 8.0
print(Employee['CGPA'])

Employee['Age'] = 24
print(Employee['Age'])

phone = input("phone number: ")

digits_mapping = {
    '1' : "one",
    '2' : "two",
    '3' : "three",
    '4' : "four",
    '5' : "five",
    '6' : "six",
    '7' : "seven",
    '8' : "eight",
    '9' : "nine",
    '0' : "ten"
}

output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
    
print(output)

#Exceptions

try:
    age = int(input("Age: "))
    print(age)
    income = 250000
    risk = income/age
    print(risk)
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Division by zero trap activated!")

