from alchemy import potions


def ft_distillation_0() -> None:
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    print(f"Testing strength_potion: {potions.strength_potion()}")
    print(f"Testing healing_potion: {potions.healing_potion()}\n")


if __name__ == "__main__":
    ft_distillation_0()
