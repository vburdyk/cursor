class Animals:

    def __init__(self, firstname, lastname, weight, eyes):
        self.name = firstname + " " + lastname
        self.weight = weight
        self.eyes = eyes

    def eat(self):
        print(self.name + " with " + self.eyes + " eyes and weight " + self.weight + " is eat!")

    def sleep(self):
        print(self.name + " with " + self.eyes + " eyes and weight " + self.weight + " is sleeping!")


class Human:
    def __init__(self, firstname, lastname, weight, eyes):
        self.name = firstname + " " + lastname
        self.weight = weight
        self.eyes = eyes

    def eat(self):
        print(self.name + " with " + self.eyes + " eyes and weight " + self.weight + " is eating!")

    def sleep(self):
        print(self.name + " with " + self.eyes + " eyes and weight " + self.weight + " is sleeping!")

    def study(self):
        print(self.name + " with " + self.weight + " weight and eyes " + self.eyes + " is studying!")

class Centaur(Human, Animals):
    pass

centaur = Centaur("Олаф", "Шольц", "80 kg", "brown")
centaur.eat()
centaur.study()