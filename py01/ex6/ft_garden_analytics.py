def count_exact_type(plants: list, target_class: type) -> int:
    count = 0
    for plant in plants:
        if type(plant) is target_class:
            count += 1
    return count


class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_description(self) -> str:
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color

    def get_description(self) -> str:
        return f"{self.name}: {self.height}cm, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str,
                 points: int) -> None:
        super().__init__(name, height, color)
        self.points = points

    def get_description(self) -> str:
        base_desc = super().get_description()
        return f"{base_desc}, Prize points: {self.points}"


class Garden:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants = []
        self.total_growth_events = 0

    def add_plant(self, plant: Plant, silent: bool = False) -> None:
        self.plants.append(plant)
        if not silent:
            print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growth_events += 1

    def report(self) -> None:
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.get_description()}")


class GardenManager:
    total_gardens_managed = 0

    def __init__(self) -> None:
        self.network = {}

    def get_garden(self, owner: str) -> Garden:
        return self.network.get(owner)

    def _create_network(cls, owners: list[str]) -> "GardenManager":
        manager = cls()
        for owner in owners:
            manager.network[owner] = Garden(owner)
            cls.total_gardens_managed += 1
        return manager

    create_garden_network = classmethod(_create_network)

    def _validate(height: int) -> bool:
        return height > 0

    validate_height = staticmethod(_validate)

    def garden_score(self, owner: str) -> int:
        garden = self.get_garden(owner)
        if not garden:
            print("Manager name doesn't exist!!")
            return 0

        total_height = 0
        for plant in garden.plants:
            total_height += plant.height
        return total_height + 40

    class GardenStats:
        def calculate(self, garden: Garden) -> dict:
            reg = count_exact_type(garden.plants, Plant)
            flow = count_exact_type(garden.plants, FloweringPlant)
            prize = count_exact_type(garden.plants, PrizeFlower)

            return {
                "count": len(garden.plants),
                "growth": garden.total_growth_events,
                "types": (reg, flow, prize)
            }


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    manager = GardenManager.create_garden_network(["Alice", "Bob"])

    alice_garden = manager.get_garden("Alice")
    bob_garden = manager.get_garden("Bob")

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
    lavender = FloweringPlant("Lavender", 20, "purple")
    corn = Plant("Corn", 32)

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    bob_garden.add_plant(corn, silent=True)
    bob_garden.add_plant(lavender, silent=True)

    print()
    alice_garden.grow_all()
    print()
    alice_garden.report()
    print()

    stats_helper = GardenManager.GardenStats()
    stats = stats_helper.calculate(alice_garden)

    print(f"Plants added: {stats['count']}, "
          f"Total growth: {stats['growth']}cm")

    regular, flowering, prize = stats["types"]
    print(f"Plant types: {regular} regular, {flowering} flowering, {prize}"
          f" prize flowers")

    print(f"\nHeight validation test: {GardenManager.validate_height(10)}")

    alice_score = manager.garden_score("Alice")
    bob_score = manager.garden_score("Bob")
    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")

    print(f"Total gardens managed: {GardenManager.total_gardens_managed}")
