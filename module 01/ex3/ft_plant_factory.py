from typing import List, Dict, Union


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = float(height)
        self.age = age


def ft_plant_factory() -> None:
    plants: List[Dict[str, Union[str, int]]] = [
        {"name": "Rose", "height": 25, "age": 30},
        {"name": "Oak", "height": 200, "age": 365},
        {"name": "Cactus", "height": 5, "age": 90},
        {"name": "Sunflower", "height": 80, "age": 45},
        {"name": "Fern", "height": 15, "age": 120},
    ]
    garden = []
    print("=== Plant Factory Output ===")
    for plant in plants:
        new_plant = Plant(
            str(plant['name']),
            float(plant['height']),
            int(plant['age'])
        )
        garden.append(new_plant)
        print(
            f"Created: {new_plant.name}: "
            f"{new_plant.height}cm, {new_plant.age} days old"
        )


if __name__ == "__main__":
    ft_plant_factory()
