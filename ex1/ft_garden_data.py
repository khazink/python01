class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


def main() -> None:
    print("=== Garden Plant Registry ===")
    p1 = Plant("Rose", 25, 30)
    print(p1.name, ":", p1.height, "cm,", p1.age, "days old")
    p2 = Plant("Sunflower", 80, 45)
    print(p2.name, ":", p2.height, "cm,", p2.age, "days old")
    p3 = Plant("Cactus", 15, 120)
    print(p3.name, ":", p3.height, "cm,", p3.age, "days old")


if __name__ == "__main__":
    main()
