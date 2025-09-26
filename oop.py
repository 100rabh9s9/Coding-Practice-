#A simple Python class to demonstrate Object-Oriented Programming (OOP).
class Student: #New Class , "the blueprint"
    def __init__(self, name, marks): #A constructor method that gets called automatically when you create an object.
        self.name = name  #Assigns the passed value
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

s1 = Student("Alice", 85)  #Object Creation
s1.display() #calling Method

