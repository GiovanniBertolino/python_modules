import alchemy.transmutation.recipes


def ft_transmutation_0() -> None:
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    e = alchemy.transmutation.recipes.lead_to_gold()
    print(f"Testing lead to gold: {e}\n")


if __name__ == "__main__":
    ft_transmutation_0()
