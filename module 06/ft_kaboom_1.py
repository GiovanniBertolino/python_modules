def ft_kaboom_1() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    from alchemy.grimoire.dark_spellbook import dark_spell_record
    name = "DARK"
    ingredients = "bats, earth and fire"
    print(
        f"Testing record light spell: {dark_spell_record(name, ingredients)}\n"
        )


if __name__ == "__main__":
    ft_kaboom_1()
