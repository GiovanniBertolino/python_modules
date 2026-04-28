import alchemy


def ft_alembic_4() -> None:
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    print("Testing hidden create_earth: ", end="")
    print(alchemy.create_earth())  # type: ignore


if __name__ == "__main__":
    ft_alembic_4()
