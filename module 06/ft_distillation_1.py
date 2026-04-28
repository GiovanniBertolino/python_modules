import alchemy


def ft_distillation_1() -> None:
    print("=== Distillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")
    print(f"Testing strength_potion: {alchemy.strength_potion()}")
    print(f"Testing heal alias: {alchemy.heal()}\n")


if __name__ == "__main__":
    ft_distillation_1()
