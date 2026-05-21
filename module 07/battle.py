from ex0 import FlameFactory, AquaFactory, CreatureFactory


def factory(object_factory: CreatureFactory) -> None:
    print("\nTesting factory")
    base = object_factory.create_base()
    evolved = object_factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("\nTesting battle")
    creature1 = factory1.create_base()
    creature2 = factory2.create_base()
    print(
        f"{creature1.describe()}\n vs.\n{creature2.describe()}"
        )
    print(" fight!")
    print(creature1.attack())
    print(creature2.attack())


def main() -> None:
    factory(FlameFactory())
    factory(AquaFactory())
    battle(FlameFactory(), AquaFactory())


if __name__ == "__main__":
    main()
