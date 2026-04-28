from typing import cast
from abc import ABC, abstractmethod
from ex0 import Creature
from ex1 import TransformCapability, HealCapability


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        ...

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError(
                f"Battle error, aborting tournament: "
                f"Invalid Creature '{creature.name}' "
                f"for this normal strategy"
                )
        print(creature.attack())

    def is_valid(self, creature: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError(
                f"Battle error, aborting tournament: "
                f"Invalid Creature '{creature.name}' "
                f"for this aggressive strategy"
                )
        t = cast(TransformCapability, creature)
        print(t.transform())
        print(creature.attack())
        print(t.revert())

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError(
                f"Battle error, aborting tournament: "
                f"Invalid Creature '{creature.name}' "
                f"for this defensive strategy"
                )
        h = cast(HealCapability, creature)
        print(creature.attack())
        print(h.heal())

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)
