#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = float(height)
        self.age = age

    def grow(self) -> None:
        self.height += 2.1

    def age_one_day(self) -> None:
        self.age += 1


class Flower(Plant):
    def __init__(
        self, name: str, height: float, age: int, color: str
    ) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.blooming = False

    def bloom(self) -> None:
        self.blooming = True

    def get_info(self) -> None:
        status = (
            f" {self.name} is blooming beautifully!"
            if self.blooming
            else f" {self.name} has not bloomed yet"
        )
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        print(f" Color: {self.color}")
        print(status)


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = float(trunk_diameter)

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height}cm long and {self.trunk_diameter}cm wide."
        )

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        print(f" Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str,
        nutritional_value: int,
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def grow(self) -> None:
        self.height = round(self.height + 2.1, 1)
        self.nutritional_value += 1

    def age_one_day(self) -> None:
        self.age += 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.get_info()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.get_info()

    print("\n=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.get_info()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5, 10, "April", 0)
    tomato.get_info()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age_one_day()
    tomato.get_info()


if __name__ == "__main__":
    ft_plant_types()
