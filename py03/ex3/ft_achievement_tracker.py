import random

ACHIEVEMENT_POOL = [
    "Crafting Genius", "World Savior", "Master Explorer",
    "Collector Supreme", "Untouchable", "Boss Slayer",
    "Strategist", "Unstoppable", "Speed Runner", "Survivor",
    "Treasure Hunter", "First Steps", "Sharp Mind", "Hidden Path Finder"
]


def gen_player_achievements() -> set[str]:
    num_achievements = random.randint(5, 9)
    chosen_achievements = random.sample(ACHIEVEMENT_POOL, num_achievements)

    return set(chosen_achievements)


def main() -> None:
    print("=== Achievement Tracker System ===")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    players = {
        "Alice": alice,
        "Bob": bob,
        "Charlie": charlie,
        "Dylan": dylan
    }

    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")

    all_distinct = alice.union(bob, charlie, dylan)

    print(f"All distinct achievements: {all_distinct}")

    common = alice.intersection(bob, charlie, dylan)
    print(f"Common achievements: {common}")

    for name, achievements in players.items():
        others_achievements: set[str] = set()
        for other_name, other_achievements in players.items():
            if name != other_name:
                others_achievements = others_achievements.union(
                    other_achievements)

        unique_to_player = achievements.difference(others_achievements)
        print(f"Only {name} has: {unique_to_player}")

    total_possible = set(ACHIEVEMENT_POOL)
    for name, achievements in players.items():
        missing = total_possible.difference(achievements)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()
