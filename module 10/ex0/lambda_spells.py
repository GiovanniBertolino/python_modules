def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda y: y['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda z:  "* " + z + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    power = list(map(lambda y: y['power'], mages))
    minpower = min(power)
    max_power = max(power)
    average = round(sum(power) / len(power), 2)
    return {
        'max_power': int(max_power),
        'min_power': int(minpower),
        'avg_power': float(average)
        }


def main() -> None:
    artifacts = [
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
        {'name': 'Crystal Orb', 'power': 85, 'type': 'orb'}
    ]
    sorted_artifacts = artifact_sorter(artifacts)
    print("\nTesting artifact sorter...")
    print(
        f"{sorted_artifacts[0]['name']} "
        f"({sorted_artifacts[0]['power']} power) comes before "
        f"{sorted_artifacts[1]['name']} "
        f"({sorted_artifacts[1]['power']} power)\n"
        )
    print("Testing spell transformer...")
    spells = ["fireball", "heal", "shield"]
    sorted_spells = spell_transformer(spells)
    print(" ".join(sorted_spells))


if __name__ == "__main__":
    main()
