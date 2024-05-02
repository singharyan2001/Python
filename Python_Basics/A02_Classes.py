"""Topics - Classes, Constructors, Inheritance"""
'''
Basic data types - Numbers(int, float, double), Strings(str), Booleans(true,false)
Complex data types - Lists, tuples, dictionaries
'''
#Classes

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def move(self):
        print("move")
    
    def draw(self):
        print("draw")



api = Point(0,0)

api.x = 40
api.y = 70

api.draw()
print(api.x)

#Constructors
point = Point(10,20)
point.x = 11
print(point.x)  #AttributeError #After creating a constructor, it will o longer be an error.


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
    def age(self):
        self.a = input("Enter age: ")
        return self.a
    
    def Intro_Person(self):
        print(f"Hi, I'm {self.fname} {self.lname}")


person = Person("Aryan", "Singh")

#age = person.age()
#print(age)

person.Intro_Person()

#Inheritance
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def meow(self):
        print("meow")


dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()
cat1.meow()

