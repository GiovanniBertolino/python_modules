from ex0 import FlameFactory, AquaFactory, CreatureFactory, Creature


def factory(object_factory: CreatureFactory) -> None:
    print("\nTesting factory")
    base = object_factory.create_base()
    evolved = object_factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def battle(creature1: Creature, creature2: Creature) -> None:
    print("\nTesting battle")
    print(
        f"{creature1.describe()}\n vs.\n{creature2.describe()}"
        )
    print(" fight!")
    print(creature1.attack())
    print(creature2.attack())


def main() -> None:
    factory(FlameFactory())
    factory(AquaFactory())
    battle(FlameFactory().create_base(), AquaFactory().create_base())


if __name__ == "__main__":
    main()
