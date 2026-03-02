class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        print(
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
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
             "{harvest_season}"
        print(f"{self.name} is rich in {nutritional_value")


def main():
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 25, 30, "red")
    rose.bloom()
    oak = Tree("Oak", 500, 1825, 50)
    oak.produce_shade()
    tomato = Vegetable("tomato", 80, 90, "summer", "vitamin C")

if __name__ == "__main__":
    main()

