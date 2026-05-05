#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = float(height)
        self.age = age
        self._grow_count = 0
        self._age_count = 0
        self._show_count = 0

    def grow(self, amount: float) -> None:
        self.height += amount
        self._grow_count += 1

    def age_days(self, days: int) -> None:
        self.age += days
        self._age_count += 1

    def get_info(self) -> None:
        self._show_count += 1
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def get_stats(self) -> None:
        print(
            f"Stats: {self._grow_count} grow, "
            f"{self._age_count} age, {self._show_count} show"
        )

    @staticmethod
    def is_more_than_a_year(days: int) -> bool:
        return days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0, 0)


class FloweringPlant(Plant):
    def __init__(
        self, name: str, height: float, age: int, color: str
    ) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.blooming = False

    def bloom(self) -> None:
        self.blooming = True

    def get_info(self) -> None:
        super().get_info()
        print(f" Color: {self.color}")
        status = (
            f" {self.name} is blooming beautifully!"
            if self.blooming
            else f" {self.name} has not bloomed yet"
        )
        print(status)


class PrizeFlower(FloweringPlant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
        seeds: int,
    ) -> None:
        super().__init__(name, height, age, color)
        self.seeds = seeds

    def get_info(self) -> None:
        super().get_info()
        print(f" Seeds: {self.seeds}")

    def grow(self, amount: float) -> None:
        super().grow(amount)
        self.seeds += int(amount)

    def age_days(self, days: int) -> None:
        super().age_days(days)
        self.seeds += 12

    def get_stats(self) -> None:
        print(
            f"Stats: {self._grow_count} grow, "
            f"{self._age_count} age, {self._show_count} show"
        )


class TreePlant(Plant):
    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = float(trunk_diameter)
        self._shade_count = 0

    def get_info(self) -> None:
        super().get_info()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        self._shade_count += 1
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height}cm long and {self.trunk_diameter}cm wide."
        )

    def get_stats(self) -> None:
        print(
            f"Stats: {self._grow_count} grow, "
            f"{self._age_count} age, {self._show_count} show "
            f"{self._shade_count} shade"
        )


def ft_garden_analytics() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(
        f"Is 30 days more than a year? -> "
        f"{Plant.is_more_than_a_year(30)}"
    )
    print(
        f"Is 400 days more than a year? -> "
        f"{Plant.is_more_than_a_year(400)}"
    )
    print("\n=== Flower")
    rose = FloweringPlant("Rose", 15, 10, "red")
    rose.get_info()
    print("[statistics for Rose]")
    rose.get_stats()
    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.get_info()
    print("[statistics for Rose]")
    rose.get_stats()
    print("\n=== Tree")
    oak = TreePlant("Oak", 200, 365, 5)
    oak.get_info()
    print("[statistics for Oak]")
    oak.get_stats()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    oak.get_stats()
    print("\n=== Seed")
    sunflower = PrizeFlower("Sunflower", 80, 45, "yellow", 0)
    sunflower.get_info()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age_days(20)
    sunflower.bloom()
    sunflower.get_info()
    print("[statistics for Sunflower]")
    sunflower.get_stats()
    print("\n=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.get_info()
    print("[statistics for Unknown plant]")
    unknown.get_stats()


if __name__ == "__main__":
    ft_garden_analytics()
