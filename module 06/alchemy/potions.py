from alchemy.elements import create_earth, create_air
from elements import create_fire, create_water


def healing_potion() -> str:
    part1 = create_earth()
    part2 = create_air()
    return f"Healing potion brewed with '{part1}' and '{part2}'"


def strength_potion() -> str:
    part1 = create_fire()
    part2 = create_water()
    return f"Strength potion brewed with '{part1}' and '{part2}'"
