class GardenManager:
    total_gardens = 0

    class GardenStats:
        @staticmethod
        def analyze_growth(plants):
            return len(plants)

        @staticmethod
        def count_types(plants):
            regular = 0
            flowering = 0
            prize = 0
            for p in plants:
                if isinstance(p, PrizeFlower):
                    prize += 1
                elif isinstance(p, FloweringPlant):
                    flowering += 1
                elif isinstance(p, Plant):
                    regular += 1
            return regular, flowering, prize

        @staticmethod
        def calculate_score(plants):
            score = 0
            for p in plants:
                score += p.height
                if hasattr(p, 'points'):
                    score += p.points
                if isinstance(p, FloweringPlant):
                    score += 15
            return score

    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        GardenManager.total_gardens += 1

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}")

    def grow_all(self):
        print(f"{self.owner} is helping all plants...")
        for plant in self.plants:
            plant.grow()

    def generate_report(self):
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"-{plant}")
        growth = self.GardenStats.analyze_growth(self.plants)
        reg, flow, prize = self.GardenStats.count_types(self.plants)
        print(f"\nPlants added: {len(self.plants)}, Total growth: {growth}cm")
        print(f"Plant types: {reg} regular, {flow} flowering, "
              "{prize} prize flower")
        print("-" * 40)

    @classmethod
    def create_garden_network(cls, owners: str) -> None:
        return [cls(owner) for owner in owners]

    @staticmethod
    def verify_height(height):
        return height > 0


class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color

    def __str__(self) -> str:
        return f"{super().__str__()}, {self.color} flowers(blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str,
                 prize_pt: int) -> None:
        super().__init__(name, height, color)
        self.prize_pt = prize_pt

    def __str__(self) -> str:
        return f"{super().__str__()}, Prize points: {self.prize_pt}"


def main() -> None:
    print("=== Garden Management System Demo ===\n")
    alice_garden = GardenManager("Alice")
    p1 = Plant("Oak Tree", 100)
    p2 = FloweringPlant("Rose", 25, "red")
    p3 = PrizeFlower("Sunflower", 51, "yellow", 10)
    alice_garden.add_plant(p1)
    alice_garden.add_plant(p2)
    alice_garden.add_plant(p3)
    print("")
    alice_garden.grow_all()
    alice_garden.generate_report()
    bob_garden = GardenManager("Bob")
    bob_garden.add_plant(Plant("Bush", 80))
    print(f"Height validation test: {GardenManager.verify_height(10)}")
    alice_score = alice_garden.GardenStats.calculate_score(alice_garden.plants)
    bob_score = 92
    print(f"Garden scores - Alice: {alice_score}, Bob {bob_score}")
    print(f"Total gardens managed: {GardenManager.total_gardens}")


if __name__ == "__main__":
    main()
