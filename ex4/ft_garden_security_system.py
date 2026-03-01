class SecurePlant:
    def __init__(self, name):
        self.name = name
        self.__height = 0
        self.__age = 0
        print(f"Plant created: {self.name}")

    def set_height(self, height):
        if height > 0:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age):
        if age > 0:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self):
        print(f"Current height is {self.__height}")

    def get_age(self):
        print(f"Current age is {self.__age}")

    def get_info(self):
        print(f"Current plant: {self.name} ({self.__height}cm, {self.__age}"
              " days)")


def main():
    print("=== Garden Security System ===")
    p1 = SecurePlant("Rose")
    p1.set_height(25)
    p1.set_age(30)
    p1.set_height(-5)
    p1.get_info()


if __name__ == "__main__":
    main()
