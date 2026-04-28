class Plant:
    """Blueprint for a garden plant."""

    def __init__(self, name: str, height: float, age: int) -> None:
        """Initialize a plant with name, height in cm, and age in days."""
        self.name = name
        self.height = float(height)
        self.age = age

    def grow(self) -> None:
        """Grow the plant by 0.8cm."""
        self.height += 0.8

    def age_one_day(self) -> None:
        """Age the plant by one day."""
        self.age += 1

    def get_info(self) -> str:
        """Return a formatted string with plant info."""
        return f"{self.name}: {self.height:.1f}cm, {self.age} days old"


def ft_plant_growth() -> None:
    """Simulate a week of plant growth."""
    rose = Plant("Rose", 25, 30)
    print("=== Garden Plant Growth ===")
    print(rose.get_info())
    initial_height = rose.height
    for day in range(1, 8):
        rose.grow()
        rose.age_one_day()
        print(f"=== Day {day} ===")
        print(rose.get_info())
    growth = rose.height - initial_height
    print(f"Growth this week: {growth:.1f}cm")


if __name__ == "__main__":
    ft_plant_growth()
