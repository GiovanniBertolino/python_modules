from alchemy.grimoire.light_spellbook import light_spell_record


def ft_kaboom_0() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    name = "Fantasy"
    ingredients = "Earth, wind and fire"
    print(
        f"Testing record light spell: {light_spell_record(name, ingredients)}"
        )
    print()


if __name__ == "__main__":
    ft_kaboom_0()
