class SecurePlant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = float(height)
        self._age = (age)
        print(
            f"Plant created: {self.name}: "
            f"{self._height}cm, {self._age} days old\n"
        )

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = float(height)
        print(f"Height updated: {int(self._height)}cm")

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = age
        print(f"Age updated: {self._age} days")


def ft_garden_security():
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 15, 10)
    plant.set_height(25)
    plant.set_age(30)
    print()
    plant.set_height(-5)
    plant.set_age(-60)
    print()
    print(
        f"Current state: {plant.name}: "
        f"{plant.get_height()}cm, {plant.get_age()} days old"
    )


if __name__ == "__main__":
    ft_garden_security()
