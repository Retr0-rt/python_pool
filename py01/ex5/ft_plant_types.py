class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> None:
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, "
              f"{self.color} color")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> None:
        shade = int(3.14 * (self.height / 100) ** 2)
        print(f"{self.name} provides {shade} square meters of shade")

    def get_info(self) -> None:
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, "
              f"{self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 nutritional_value: str, harvest_season: str) -> None:

        super().__init__(name, height, age)
        self.nutritional_value = nutritional_value
        self.harvest_season = harvest_season

    def get_info(self) -> None:
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
              f"{self.harvest_season} harvest")
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")

    rose = Flower("rose", 25, 30, "red")
    oak = Tree("oak", 500, 1825, 50)
    tomato = Vegetable("tomato", 80, 90, "vitamin C", "summer")

    tulip = Flower("tulip", 15, 27, "yellow")
    olive = Tree("olive", 980, 1900, 20)
    potato = Vegetable("potato", 40, 60, "carbohydrates", "autumn")

    rose.get_info()
    rose.bloom()
    print()

    oak.get_info()
    oak.produce_shade()
    print()

    tomato.get_info()
    print()
