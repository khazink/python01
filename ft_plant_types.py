class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom():
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
       super().__init__(name, height, age)
       self.trunk_dia = trunk_diameter

    def produce_shade():
        print(f"{self.name} provide {self.trunk_dia * self.trunk_dia * 3.14}"
              " square meters of shade")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season

    def nutritional_value()
        print(f"{self.name} is rich in vitamin C)
        
