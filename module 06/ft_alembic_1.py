from elements import create_water


def ft_alembic_1() -> None:
    print("=== Alembic 1 ===")
    print("Using: 'from ... import ...' structure to access elements.py")
    print(f"Testing create_water: {create_water()}\n")


if __name__ == "__main__":
    ft_alembic_1()
