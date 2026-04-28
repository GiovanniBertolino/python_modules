from alchemy import elements


def ft_alembic_3() -> None:
    print("=== Alembic 3 ===")
    print(
        "Accessing alchemy/elements.py using 'from ... import ...' structure"
        )
    print(f"Testing create_air: {elements.create_air()}\n")


if __name__ == "__main__":
    ft_alembic_3()
