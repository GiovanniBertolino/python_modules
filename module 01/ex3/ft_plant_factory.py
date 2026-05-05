#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = float(height)
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_plant_factory() -> None:
    print("=== Plant Factory Output ===")

    plants = [
        Plant("rose", 25.0, 30),
        Plant("oak", 200.0, 365),
        Plant("cactus", 5.0, 90),
        Plant("sunflower", 80.0, 45),
        Plant("fern", 15.0, 120)
    ]

    for plant in plants:
        print("Created:", end=" ")
        plant.show()


if __name__ == "__main__":
    ft_plant_factory()
