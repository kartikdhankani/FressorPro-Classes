#Date - 22.06.20 
# class
# class is the blueprint of the object 
# object is teh instance of the class

#attribute - 
#Type 1 attribute - class attribute - COmmon attributes like Colour of eyes: Black, Red, Blue, Yellow, brown
#type 2 attribute - Instance attribute - Unique attribute like Name of student

class student:
    dress_code='Black_white'     #These are class attributes
    school_name='Xaviers'
    subjects='pcm'

    def __init__(self, name, gmail, roll_no):
        self.name = name         #These are Instance attribute; unique for all objects
        self.gmail = gmail
        self.roll_no = roll_no

    def about_me(self):
        return f'my name is {self.name}'

obj1=student('matt','matt@gmail.com',55)
obj2=student('Sam','sam@gmail.com',60)
print(obj1.name,obj1.gmail,obj1.roll_no)

print(obj1.about_me())
print(obj2.about_me())

#Let's understand method now,
#Method means a function within a class

#init method is a constructore; it's executed automatically when you create an object.

#Exercise - Create a class called "Circle"; it will have 

class Circle_new:
    pi=3.14

    def __init__(self,radius):     #Write double ##
        self.radius=radius
    
    def circumference(self):
        return 2*self.pi*self.radius

    def area(self):
        return self.pi*(self.radius**2)
    
c1=Circle_new(5)
c2=Circle_new(10)

print(c1.radius)
print(c2.radius)

print(c1.area())
print(c2.area())

#Exercise - Create a class with the name book and instance attributes - Titles, qty, author, etc.

class Book:

    def __init__(self,title,author,price,qty):
        self.title=title
        self.author=author
        self.price=price
        self.qty=qty

    def get_price(self):
        return self.price
    
    def set_price(self,new_price):
        self.price=new_price

    
b1=Book(title="1984",author="George",price=29.99,qty=100)

print(b1.author)
b1.set_price(45)
print(b1.price)


#Clas = Bank A/C (Class Att. = Bank Name, Ins. Att. = A/C No., Balance, & Methods = init, deposit, )

