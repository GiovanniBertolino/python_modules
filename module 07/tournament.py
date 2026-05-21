from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy, NormalStrategy
from ex2 import AggressiveStrategy, DefensiveStrategy


def battle(opponants: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    for i in range(len(opponants)):
        for j in range(i + 1, len(opponants)):
            print("* Battle *")
            factory_a, strategy_a = opponants[i]
            factory_b, strategy_b = opponants[j]
            creature_a = factory_a.create_base()
            creature_b = factory_b.create_base()
            print(creature_a.describe())
            print(" vs.")
            print(creature_b.describe())
            print(" now fight!")
            try:
                strategy_a.act(creature_a)
                strategy_b.act(creature_b)
            except ValueError as e:
                print(e)
                return


def main() -> None:
    # Factory
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    # Strategy
    normal = NormalStrategy()
    agressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    tournament0 = [
        (flame_factory, normal),
        (healing_factory, defensive),
    ]

    tournament1 = [
        (flame_factory, agressive),
        (healing_factory, defensive)
    ]

    tournament2 = [
        (aqua_factory, normal),
        (healing_factory, defensive),
        (transform_factory, agressive)
    ]

    # Tournament 0 (basic)
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print(f"{len(tournament0)} opponents involved\n")
    battle(tournament0)

    # Tournament 1 (error)
    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print(f"{len(tournament1)} opponents involved\n")
    battle(tournament1)

    # Tournament 2 (multiple)
    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    print("*** Tournament ***")
    print(f"{len(tournament2)} opponents involved\n")
    battle(tournament2)


if __name__ == "__main__":
    main()
