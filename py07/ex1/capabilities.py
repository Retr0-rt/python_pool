from abc import ABC, abstractmethod
from ex0.CreatureFactory import Creature, CreatureFactory
from typing import Union


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: "Creature") -> str:
        pass


class TransformCapability(ABC):
    def __init__(self, isTransformed: bool = False):
        self._isTransformed: bool = isTransformed

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(Creature, HealCapability):
    def __init__(self, name: str, type: str):
        super().__init__(name, type)

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self, target: Union["Creature", None] = None):
        if target is None or target == self:
            return f"{self._name} heals itself for a small amount"
        else:
            return f"{self._name} heals {target._name} for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self, name: str, type: str):
        super().__init__(name, type)

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def heal(self, target: Union["Creature", None] = None):
        if target is None or target == self:
            return f"{self._name} heals itself and others for a large amount"
        else:
            return (f"{self._name} heals {target._name} and others for a "
                    f"large amount")


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> "Creature":
        return Sproutling(name="Sproutling", type="Grass")

    def create_evolved(self) -> Creature:
        return Bloomelle(name="Boolmelle", type="Grass/Fairy")


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str, type: str, isTransformed: bool = False):
        Creature.__init__(self, name, type)
        TransformCapability.__init__(self, isTransformed=isTransformed)

    def attack(self) -> str:
        if not self._isTransformed:
            return f"{self._name} attacks normally"
        return f"{self._name} performs a boosted strike!"

    def transform(self) -> str:
        if not self._isTransformed:
            self._isTransformed = True
            return f"{self._name} shifts into a sharper form!"
        return f"{self._name} already in the Transformed form"

    def revert(self) -> str:
        if self._isTransformed:
            self._isTransformed = False
            return f"{self._name} returns to normal."
        return f"{self._name} already in normal form"


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str, type: str, isTransformed: bool = False):
        Creature.__init__(self, name, type)
        TransformCapability.__init__(self, isTransformed=isTransformed)

    def attack(self) -> str:
        if not self._isTransformed:
            return f"{self._name} attacks normally"
        return f"{self._name} unleashes a devastating morph strike!"

    def transform(self) -> str:
        if not self._isTransformed:
            self._isTransformed = True
            return f"{self._name} morphs into a dragonic battle form!"
        return f"{self._name} already in the Transformed form"

    def revert(self) -> str:
        if self._isTransformed:
            self._isTransformed = False
            return f"{self._name} stabilizes its form."
        return f"{self._name} already in normal form"


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling(name="Shiftling", type="Normal")

    def create_evolved(self) -> Creature:
        return Morphagon(name="Morphagon", type="Normal/Dragon")
