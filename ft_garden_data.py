class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        print(self.name, ":", self.height, "cm,", self.age, "days old")

def main():
    print("=== Garden Plant Registry ===")
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)
    p3 = Plant("Cactus", 15, 120)

if __name__ == "__main__":
    main()
