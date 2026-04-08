from ex0 import *

def test_factory(factory: CreatureFactory) -> None:

    print("\nTesting factory")

    base_creature = factory.create_base()
    print(base_creature.describe())
    print(base_creature.attack())

    evolved_creature = factory.create_evolved()
    print(evolved_creature.describe())
    print(evolved_creature.attack())


def test_battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    
    print("\nTesting battle")

    base_creature1 = factory1.create_base()
    base_creature2 = factory2.create_base()

    print(base_creature1.describe())
    print("vs")
    print(base_creature2.describe())

    print("fight!")

    print(base_creature1.attack())
    print(base_creature2.attack())

if __name__ == "__main__":
    Fire_factory = FlameFactory()
    Water_factory = AquaFactory()

    test_factory(Fire_factory)
    test_factory(Water_factory)
    test_battle(Fire_factory, Water_factory)
