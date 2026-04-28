from ex0 import Creature
from .capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self):
        super().__init__(name="Sproutling", type="Grass")

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self):
        super().__init__(name="Bloomelle", type="Grass/Fairy")

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self):
        super().__init__(name="Shiftling", type="Normal")
        self.state = False

    def attack(self) -> str:
        if self.state:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self.state = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.state = False
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self):
        super().__init__(name="Morphagon", type="Normal/Dragon")
        self.state = False

    def attack(self) -> str:
        if self.state:
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self.state = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.state = False
        return f"{self.name} stabilizes its form."
