import functools
from collections.abc import Callable
import time


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"Casting {func.__name__}...")
        result = func(*args, **kwargs)
        end = time.time()
        elapsed = end - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if 'power' in kwargs:
                power = kwargs['power']
            elif len(args) > 2:
                power = args[2]
            elif len(args) > 1:
                power = args[1]
            else:
                power = args[0]
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            trys = 0
            while trys < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    trys += 1
                    if trys < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {trys}/{max_attempts})"
                            )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild():
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c == " " for c in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("Testing spell timer...")

    @spell_timer
    def fireball():
        time.sleep(0.101)
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}\n")
    print("Testing retrying spell...")

    @retry_spell(3)
    def unstable_spell() -> str:
        raise Exception("Spell unstable!")

    result = unstable_spell()
    print(f"{result}")

    @retry_spell(3)
    def stable_spell():
        return "Waaaaaaagh spelled !"

    print(f"{stable_spell()}\n")
    print("Testing MageGuild...")

    guild = MageGuild()
    print(guild.validate_mage_name("harry potter"))
    print(guild.validate_mage_name("a"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()
