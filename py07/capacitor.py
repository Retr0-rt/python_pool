from ex1.Capabilities import HealingCreatureFactory, TransformCreatureFactory
from ex1.Capabilities import HealCapability, TransformCapability
from typing import cast

def test_healing_factory():
    factory = HealingCreatureFactory()

    print("Testing Creature with healing capability")
    print("base:")
    base = factory.create_base()

    print(base.describe())
    print(base.attack())
    if (isinstance(base, HealCapability)):
        print(base.heal())


    print("evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    if(isinstance(evolved, HealCapability)):
        print(evolved.heal())


def test_transforming_factory():
    factory = TransformCreatureFactory()

    print("\nTesting Creature with transform capability")
    print("base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    if(isinstance(base, TransformCapability)):
        print(base.transform())
        print(base.attack())
        print(base.revert())

    print("evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    if(isinstance(evolved, TransformCapability)):
        print(evolved.transform())
        print(evolved.attack())
        print(evolved.revert())


if __name__ == "__main__":
    test_healing_factory()
    test_transforming_factory()
