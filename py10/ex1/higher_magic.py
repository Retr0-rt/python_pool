from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))

    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_spell(target: str, power: int) -> str:
        amplified_power = power * multiplier
        return base_spell(target, amplified_power)

    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence_spell(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]

    return sequence_spell


if __name__ == "__main__":
    # --- Sample Spells and Conditions for Testing ---
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target}"

    def heal(target: str, power: int) -> str:
        return f"Heals {target}"

    def needs_healing(target: str, power: int) -> bool:
        # Example condition: only heal allies
        return target == "Ally"

    print("\nTesting spell combiner...")
    combo_spell = spell_combiner(fireball, heal)
    result_tuple = combo_spell("Dragon", 50)
    print(f"Combined spell result: {result_tuple[0]}, {result_tuple[1]}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    base_power = 10
    amplified_power = base_power * 3
    print(f"Original: {base_power}, Amplified: {amplified_power}")

    # print("\nTesting conditional caster...")
    # smart_heal = conditional_caster(needs_healing, heal)
    # print(f"Casting on Ally: {smart_heal('Ally', 20)}")
    # print(f"Casting on Enemy: {smart_heal('Enemy', 20)}")

    # print("\nTesting spell sequence...")
    # routine = spell_sequence([fireball, heal, mega_fireball])
    # results = routine("Training Dummy", 15)
    # for res in results:
    #     print(f"- {res}")
