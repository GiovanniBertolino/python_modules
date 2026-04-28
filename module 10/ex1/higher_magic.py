from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        res1 = spell1(target, power)
        res2 = spell2(target, power)
        return (res1, res2)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier(target: str, power: int) -> str:
        new_spell = base_spell(target, power*multiplier)
        return new_spell
    return amplifier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list:
        results = list(map(lambda s: s(target, power), spells))
        return results
    return sequence


def main() -> None:
    print("\nTesting spell combiner...")

    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target}"

    def heal(target: str, power: int) -> str:
        return "Fireball Heals"

    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 5)
    print(f'Combined spell result: {", ".join(result)}')
    print("\nTesting power amplifier...")
    power = 10
    amplifier = 3
    mega_fireball = power_amplifier(fireball, amplifier)
    result = mega_fireball("Dragon", 10)
    print(f"Original: {power}, Amplified: {power*amplifier}")


if __name__ == "__main__":
    main()
