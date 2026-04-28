from typing import cast
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1 import HealCapability, TransformCapability


def capacitor() -> None:
    print("Testing Creature with healing capability")
    healing = HealingCreatureFactory()
    sproutling = healing.create_base()
    s = cast(HealCapability, sproutling)
    bloomelle = healing.create_evolved()
    b = cast(HealCapability, bloomelle)
    print(" base:")
    print(sproutling.describe())
    print(sproutling.attack())
    print(s.heal())
    print(" evolved:")
    print(bloomelle.describe())
    print(bloomelle.attack())
    print(b.heal())
    print("\nTesting Creature with transform capability")
    transform = TransformCreatureFactory()
    shiftling = transform.create_base()
    sh = cast(TransformCapability, shiftling)
    morphagon = transform.create_evolved()
    m = cast(TransformCapability, morphagon)
    print(" base:")
    print(shiftling.describe())
    print(shiftling.attack())
    print(sh.transform())
    print(shiftling.attack())
    print(sh.revert())
    print(" evolved:")
    print(morphagon.describe())
    print(morphagon.attack())
    print(m.transform())
    print(morphagon.attack())
    print(m.revert())


if __name__ == "__main__":
    capacitor()
