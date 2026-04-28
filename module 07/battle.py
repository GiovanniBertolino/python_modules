from ex0 import FlameFactory, AquaFactory


def battle() -> None:
    print("Testing factory")
    flame = FlameFactory()
    flameling = flame.create_base()
    pyrodon = flame.create_evolved()
    print(flameling.describe())
    print(flameling.attack())
    print(pyrodon.describe())
    print(pyrodon.attack())
    print("\nTesting factory")
    aqua = AquaFactory()
    aquabub = aqua.create_base()
    torragon = aqua.create_evolved()
    print(aquabub.describe())
    print(aquabub.attack())
    print(torragon.describe())
    print(torragon.attack())
    print("\nTesting battle")
    print(
        f"{flameling.describe()}\n vs.\n{aquabub.describe()}"
        )
    print(" fight!")
    print(flameling.attack())
    print(aquabub.attack())


if __name__ == "__main__":
    battle()
