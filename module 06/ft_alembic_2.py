import alchemy.elements


def ft_alembic_2() -> None:
    print("=== Alembic 2 ===")
    print("Accessing alchemy/elements.py using 'import ...' structure")
    print(f"Testing create_earth: {alchemy.elements.create_earth()}\n")


if __name__ == "__main__":
    ft_alembic_2()
