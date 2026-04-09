from ex2.BattleStrategy import BattleStrategy
from ex2.BattleStrategy import NormalStrategy, AggressiveStrategy, DefensiveStrategy
from ex0.CreatureFactory import Creature, CreatureFactory, FlameFactory, AquaFactory
from ex1.Capabilities import HealingCreatureFactory, TransformCreatureFactory
from itertools import combinations


def run_tournament(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    if len(opponents) < 2:
        raise ValueError("Number of opponents must be at least 2")
        return
    
    print(f"{len(opponents)} opponents involved" )
    
    created_opponnents: list[tuple[Creature, BattleStrategy]] = [(o[0].create_base(), o[1]) for o in opponents]

    try:
        for battle in list(combinations(created_opponnents, 2)):
            print("\n* Battle *")
            creature1, strategie1 = battle[0]
            creature2, strategie2 = battle[1]
            print(creature1.describe())
            print("vs.")
            print(creature2.describe())
            print("now fight!")
            print(strategie1.act(creature=creature1))
            print(strategie2.act(creature=creature2))
    
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

    run_tournament([(healer_fac, defensive), (healer_fac, defensive)])
    run_tournament([(water_fac, normal), (healer_fac, defensive), (transformer_fac, aggressive)])
