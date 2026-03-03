class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        print(f"{self.name} (Flower): {self.height}cm {self.age} days, "
              f"{self.color} color")

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_dia = trunk_diameter
        print(f"{self.name} (Tree): {self.height}cm {self.age} days, "
              f"{self.trunk_dia}cm diameter")

    def produce_shade(self) -> None:
        print(f"{self.name} provide {int(((self.height ** 2) * 3.14)/10000)}"
              " square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str, 
                 nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
             f"{harvest_season}")
        print(f"{self.name} is rich in {self.nutritional_value}")


def main() -> None:
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 25, 30, "red")
    rose.bloom()
    lily = Flower("Lily", 15, 20, "white")
    lily.bloom()
    oak = Tree("Oak", 500, 1825, 50)
    oak.produce_shade()
    walnut = Tree("Walnut", 1000, 3000, 100)
    walnut.produce_shade()
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    grape = Vegetable("Grape", 75, 56, "winter", "testosterone")

if __name__ == "__main__":
    main()

