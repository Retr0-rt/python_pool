from ex2.BattleStrategy import BattleStrategy
from ex2.BattleStrategy import NormalStrategy, AggressiveStrategy
from ex2.BattleStrategy import DefensiveStrategy
from ex0.CreatureFactory import Creature, CreatureFactory, FlameFactory
from ex0.CreatureFactory import AquaFactory
from ex1.Capabilities import HealingCreatureFactory, TransformCreatureFactory
from itertools import combinations


def run_tournament(opponents: list[tuple[CreatureFactory, BattleStrategy]]
                   ) -> None:
    print("*** Tournament ***")

    try:
        if len(opponents) < 2:
            raise ValueError("Number of opponents must be at least 2")
            return

        print(f"{len(opponents)} opponents involved")

        created_opponents: list[tuple[Creature, BattleStrategy]] = [
            (o[0].create_base(), o[1]) for o in opponents]

        for battle in combinations(created_opponents, 2):
            print("\n* Battle *")
            creature1, strategy1 = battle[0]
            creature2, strategy2 = battle[1]
            print(creature1.describe())
            print(" vs.")
            print(creature2.describe())
            print(" now fight!")
            print(strategy1.act(creature=creature1))
            print(strategy2.act(creature=creature2))

    except ValueError as e:
        print(f"Battle error, aborting tournament: {e}")
        return


if __name__ == "__main__":
    fire_fac = FlameFactory()
    water_fac = AquaFactory()
    healer_fac = HealingCreatureFactory()
    transformer_fac = TransformCreatureFactory()

    normal = NormalStrategy()
    defensive = DefensiveStrategy()
    aggressive = AggressiveStrategy()

    print("Tournament 0 (basic)\n[(Flameling+Normal), (Healing+Defensive)]")
    run_tournament([(fire_fac, normal), (healer_fac, defensive)])
    print("\nTournament 1 (error)\n[(Flameling+Aggressive),"
          " (Healing+Defensive)]")
    run_tournament([(fire_fac, aggressive), (healer_fac, defensive)])
    print("\nTournament 2 (multiple)\n[(Aquabub+Normal), (Healing+Defensive),"
          " (Transform+Aggressive)]")
    run_tournament([(water_fac, normal), (healer_fac, defensive),
                   (transformer_fac, aggressive)])
