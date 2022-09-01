# Name: Kyle Goggio
# D2L Username: 
# Date: 12/14/2021

# DO NOT CHANGE THE FILENAME: cat.py
# IMPORTANT:    Before you submit, make sure your program produces 
#               the expected result as shown in the assignment description

class Cat:
    #The Cat class must have the following:
    #A name attribute that is intialized when a cat is created.
    #An energy attribute that has an initial value of 2.
    #A stomach capacity attribute that has an initial value of 2.
    #A method called play(). If the value of energy is greater than 0, 
    #   it prints a message similar to "catname says meow" and then reduces the value of energy by 1. 
    #   The message has to contain the name of the cat and the sound meow. 
    #   However, if the value of energy is less than or equal to 0, it prints "catname is tired" instead.
    #A method called eat(). If the capacity of stomach is greater than 0, 
    #   it prints a message similar to "catname says nom" and then reduces the capacity of stomach by 1. 
    #   The message has to contain the name of the cat and the sound nom. 
    #   However, if the capacity of stomach is less than or equal to 0, it prints "catname is full" instead.
    def __init__(self, name):
        self.name = name
        self.energy = 2
        self.stomach_capacity = 2

    def play(self):
        if self.energy > 0:
            print(self.name + " says meow")
            self.energy = self.energy - 1
        elif self.energy <= 0:
            print(self.name + " is tired")

    def eat(self):
        if self.stomach_capacity > 0:
            print(self.name + " says nom")
            self.stomach_capacity = self.stomach_capacity - 1
        elif self.stomach_capacity <= 0:
            print(self.name + " is full")


print(Cat)