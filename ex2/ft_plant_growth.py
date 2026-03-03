class Plant:
    def __init__(self, name: str, height: int, day: int) -> None:
        self.name = name
        self.start = height
        self.height = height
        self.day = day

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.day += 1

    def get_info(self) -> None:
        print(self.name, ":", self.height, "cm,", self.day, "days old")


def main() -> None:
    days = 6
    rose = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    rose.get_info()
    for i in range(days):
        rose.grow()
        rose.age()
    print(f"=== Day {days + 1}  ===")
    rose.get_info()
    print(f"Growth this week: +{rose.height - rose.start}cm")


if __name__ == "__main__":
    main()
