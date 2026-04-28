import random


ALL_ACHIEVEMENTS = [
    'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
    'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
    'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
    'Boss Slayer', 'Hidden Path Finder'
]


def gen_player_achievements() -> set[str]:
    n = random.randint(4, len(ALL_ACHIEVEMENTS) - 2)
    return set(random.sample(ALL_ACHIEVEMENTS, n))


def ft_achievement_tracker() -> None:
    print("=== Achievement Tracker System ===\n")
    players: list[tuple[str, set[str]]] = [
        ("Alice", gen_player_achievements()),
        ("Bob", gen_player_achievements()),
        ("Charlie", gen_player_achievements()),
        ("Dylan", gen_player_achievements()),
    ]
    for name, achievements in players:
        print(f"Player {name}: {achievements}")

    all_achievements = set.union(*(a for _, a in players))
    print(f"\nAll distinct achievements: {all_achievements}\n")

    common = set.intersection(*(a for _, a in players))
    print(f"Common achievements: {common}\n")

    for name, achievements in players:
        others = set.union(*(a for n, a in players if n != name))
        print(f"Only {name} has: {achievements.difference(others)}")

    print()
    for name, achievements in players:
        print(
            f"{name} is missing: {all_achievements.difference(achievements)}"
            )


if __name__ == "__main__":
    ft_achievement_tracker()
