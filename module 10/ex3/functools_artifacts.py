import functools
from collections.abc import Callable
from typing import Any
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": lambda a, b:  max(a, b),
        "min": lambda a, b:  min(a, b),
    }
    if operation not in ops:
        raise ValueError("Operation is unknow")
    return functools.reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire = functools.partial(base_enchantment, 50, "Fire")
    Water = functools.partial(base_enchantment, 50, "Water")
    Wood = functools.partial(base_enchantment, 50, "Wood")
    return {"fire": fire, "Water": Water, "Wood": Wood}


@functools.lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatcher(arg) -> None:
        return "Unknown spell type"

    @dispatcher.register(int)
    def _(arg) -> None:
        return f"Damage spell: {arg} damage"

    @dispatcher.register(str)
    def _(arg) -> None:
        return f"Enchantment: {arg}"

    @dispatcher.register(list)
    def _(arg) -> None:
        return f"Multi-cast: {len(arg)} spells"
    return dispatcher


def main() -> None:
    print("\nTesting spell reducer...")
    _add = [25, 75]
    _multiply = [2, 120000]
    _maximum = [10, 32, 40]
    add = spell_reducer(_add, "add")
    multiply = spell_reducer(_multiply, "multiply")
    maximum = spell_reducer(_maximum, "max")
    print(f"Sum: {add}")
    print(f"Product: {multiply}")
    print(f"Max: {maximum}")
    print("\nTesting memoized fibonacci...")
    fibonacci1 = memoized_fibonacci(0)
    fibonacci2 = memoized_fibonacci(1)
    fibonacci3 = memoized_fibonacci(10)
    fibonacci4 = memoized_fibonacci(15)
    print(f"Fib(0): {fibonacci1}")
    print(f"Fib(1): {fibonacci2}")
    print(f"Fib(10): {fibonacci3}")
    print(f"Fib(15): {fibonacci4}")
    print("\nTesting spell dispatcher...")
    spell = spell_dispatcher()
    print(spell(42))
    print(spell("fireball"))
    print(spell(_maximum))
    print(spell(3.1))


if __name__ == "__main__":
    main()
