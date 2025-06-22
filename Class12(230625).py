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


obj1=student('matt','matt@gmail.com',55)
obj2=student('SAm','sam@gmail.com',60)
print(obj1.name,obj1.gmail,obj1.roll_no)


