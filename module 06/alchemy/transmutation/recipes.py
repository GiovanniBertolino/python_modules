import alchemy.potions
from ..elements import create_air
from elements import create_fire


def lead_to_gold() -> str:
    air = create_air()
    strength = alchemy.potions.strength_potion()
    fire = create_fire()
    r1 = "Recipe transmuting Lead to Gold: brew"
    return f"{r1}'{air}' and '{strength}' mixed with '{fire}'"
