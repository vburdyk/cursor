class Animals:

    def __init__(self, firstname, lastname, weight, eyes):
        self.name = firstname + " " + lastname
        self.weight = weight
        self.eyes = eyes

    def eat(self):
        print(self.name + " with " + self.eyes + " eyes and weight " + self.weight + " is eating!")

    def sleep(self):
        print(self.name + " with " + self.eyes + " eyes and weight " + self.weight + " is sleeping!")

class Dog(Animals):
    def bark(self):
        print(self.name + " with " + self.eyes + " eyes and weight " + self.weight + " is barking!")
    def do_tricks(self):
        print(self.name + " with " + self.eyes + " eyes and weight " + self.weight + " is doing tricks!")

class Cat(Animals):
    def meow(self):
        print(self.name + " with " + self.eyes + " eyes and weight " + self.weight + " is meowing!")
    def hunt(self):
        print("The cat is hunting")

class Monkey(Animals):
    def climb(self):
        print("The monkey is climbing")
    def steal(self):
        print(self.name + " with " + self.eyes + " eyes and weight " + self.weight + " is stealing!")

class Bird(Animals):
    def fly(self):
        print("The bird is flying")
    def sing(self):
        print(self.name + " with " + self.eyes + " eyes and weight " + self.weight + " is singing!")

class Fish(Animals):
    def swim(self):
        print("The fish is swimming")

bird = Bird("Chirick","Chirckovich", "100 gr", "brown")
bird.sing()
monkey = Monkey("Мавпа","Бананівна", "7 кг", "brown")
monkey.eat()