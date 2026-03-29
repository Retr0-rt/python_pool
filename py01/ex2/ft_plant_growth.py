class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def to_age(self) -> None:
        self.age += 1

    def grow(self) -> None:
        self.height += 1


if __name__ == "__main__":
    plant = Plant("Rose", 25, 30)
    start = 1
    end = 7

    print(f"=== Day {start} ===")
    plant.get_info()
    for i in range(start, end):
        plant.grow()
        plant.to_age()

    print(f"=== Day {end} ===")
    plant.get_info()
    print(f"Growth this week: +{end - start}cm")
