class Plant:
    def __init__(self, name, start_height, start_age):
        self.name = name
        self.height = start_height
        self.age = start_age
    def Output(self):
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")

def main():
    names = ["Rose", "Oak", "Cactus", "Sunflower", "Fern"]
    heights = [25, 200, 5, 80, 15]
    ages = [30, 365, 90, 45, 120]
    my_plant = []
    print("=== Plant Factory Output ===")
    for i in range(len(names)):
        cur_name = names[i]
        cur_height = heights[i]
        cur_age = ages[i]
        new_plant = Plant(cur_name, cur_height, cur_age)
        new_plant.Output()
        my_plant.append(new_plant)
    print(f"Total plants created: {len(my_plant)}")

if __name__ == "__main__":
    main()
