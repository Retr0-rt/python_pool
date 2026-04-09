from abc import ABC, abstractmethod
from ex0.CreatureFactory import Creature
from ex1.Capabilities import TransformCapability, HealCapability
from typing import cast


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: "Creature") -> str:
        pass

    @abstractmethod
    def is_valid(self, creature: "Creature") -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature: "Creature") -> str:
        if not self.is_valid(creature):
            raise ValueError(f"Invalid Creature '{creature._name}' for this normal strategy")
        return creature.attack()
    
    def is_valid(self, creature: Creature) -> bool:
        return True
    

class AggressiveStrategy(BattleStrategy):
    def act(self, creature: "Creature") -> str:
        if not self.is_valid(creature):
            raise ValueError(f"Invalid Creature '{creature._name}' for this aggressive strategy")
        transformer = cast(TransformCapability, creature)
        action2 = transformer.transform()
        action1 = creature.attack()
        action3 = transformer.revert()
        return f"{action1}\n{action2}\n{action3}"
    
    def is_valid(self, creature: "Creature") -> bool:
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: "Creature") -> str:
        if not self.is_valid(creature):
            raise ValueError(f"Invalid Creature '{creature._name}' for this Defensive strategy")
        healer = cast(HealCapability, creature)
        action1 = creature.attack()
        action2 = healer.heal()
        return f"{action1}\n{action2}"
    
    def is_valid(self, creature: "Creature") -> bool:
        return isinstance(creature, HealCapability)
        