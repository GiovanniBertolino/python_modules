#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = float(height)
        self.age = age

    def grow(self) -> None:
        self.height += 0.8

    def age_one_day(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


def ft_plant_growth() -> None:
    print("=== Garden Plant Growth ===")

    rose = Plant("Rose", 25, 30)
    initial_height = rose.height
    rose.show()

    for day in range(1, 8):
        rose.grow()
        rose.age_one_day()
        print(f"=== Day {day} ===")
        rose.show()

    growth = round(rose.height - initial_height, 1)
    print(f"Growth this week: {growth}cm")


if __name__ == "__main__":
    ft_plant_growth()
