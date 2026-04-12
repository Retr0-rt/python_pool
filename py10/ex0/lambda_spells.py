def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return (sorted(artifacts, key=lambda item : item["power"], reverse=True))

def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda item: item["power"] >= min_power, mages))

def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: "* "+spell+" *", spells))

def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda x: x['power'], mages))
    return {
        'max_power': max(powers),
        'min_power': min(powers),
        'avg_power': round(sum(powers) / len(powers), 2)
    }

if __name__ == "__main__":
    artifacts = [
                 {'name': 'Water Chalice', 'power': 84, 'type': 'focus'},
                 {'name': 'Fire Staff', 'power': 86, 'type': 'weapon'},
                 {'name': 'Ice Wand', 'power': 99, 'type': 'weapon'},
                 {'name': 'Shadow Blade', 'power': 95, 'type': 'weapon'}
                ]
    
    mages = [
             {'name': 'Jordan', 'power': 86, 'element': 'wind'},
             {'name': 'Alex', 'power': 73, 'element': 'earth'},
             {'name': 'Casey', 'power': 67, 'element': 'lightning'},
             {'name': 'River', 'power': 55, 'element': 'ice'},
             {'name': 'Storm', 'power': 70, 'element': 'earth'}
            ]
    
    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(
        f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} power)"
        f" comes before"
        f" {sorted_artifacts[1]['name']} "
        f"({sorted_artifacts[1]['power']} power)"
    )

    print("\nTesting spell transformer...")

    spells = ['blizzard', 'tornado', 'heal', 'earthquake']
    print(*spell_transformer(spells))
