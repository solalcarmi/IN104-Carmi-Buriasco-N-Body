class Cat:
    def __init__(self, name, color, weight, goutiere = True):
        self.name = name
        self.color = color
        self.weight = weight
        self.goutiere = goutiere

    def jump(self, height = 1):
        if height < 5 / self.weight:
            print("J'ai sauté")
        else:
            print("Trop gros")

    def brosser(self):
        print("J'ai le poil propre")


class Sphinx(Cat):
    def __init__(self, name, weight):
        super().__init__(name, "chauve", weight, False)

    def brosser(self):
        print("J'suis chauve")

    def lecher_la_peau(self):
        print("Quoi ?")


Cat.brosser()
felix = Cat("Felix", "blue", 8)
robert = Cat("Robert", "black", 5)
jimmy = Cat("Jimmy", color="red", weight=10)
bob = Sphinx("Bob", 5)
bob.jump(3)
felix.lecher_la_peau()
felix.brosser()
bob.brosser()
robert.jump()
print(robert.weight)
robert.weight = 10
print(robert.weight)
print()