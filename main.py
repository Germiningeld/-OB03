class Animal():
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

class Bird(Animal):
    def __init__(self, name, age, color:str):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        print("Чирик")

    def eat(self):
        print("Я ем зерна")

class Mammal(Animal):
    def __init__(self, name, age, size:str):
        super.__init__(name, age)
        self.size = size

    def make_sound(self):
        print("Гррр")

    def eat(self):
        print("Я ем траву")

class Reptile(Animal):
    def __init__(self, name, age, legs:bool):
        super().__init__(name, age)
        self.legs = legs

    def make_sound(self):
        print("Шшшшш")

    def eat(self):
        print("Я ем насекомых")

