class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    plants = [
        Plant("rose", 25, 30),
        Plant("sunflower", 80, 45),
        Plant("cactus", 15, 120)
    ]
    print("=== Garden Plant Registry ===")
    for plant in plants:
        print(f"{plant.name.capitalize()}: {plant.height}cm", end="")
        print(f", {plant.age} days old")
