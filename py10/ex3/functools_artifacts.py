import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    ops: dict[str, Callable] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    if operation not in ops:
        raise ValueError(
            f"Unknown operation: '{operation}'. Valid operations are: add,"
            f" multiply, max, min.")

    return functools.reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    # The base_enchantment expects: (power: int, element: str, target: str)
    # functools.partial "locks in" the first two positional arguments
    return {
        "fire": functools.partial(base_enchantment, 50, "Fire"),
        "ice": functools.partial(base_enchantment, 50, "Ice"),
        "lightning": functools.partial(base_enchantment, 50, "Lightning")
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError(
            "Fibonacci sequence is not defined for negative numbers.")
    if n == 0:
        return 0
    if n == 1:
        return 1

    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @functools.singledispatch
    def cast_spell(spell: Any) -> str:
        return "Unknown spell type"

    # We register specific handlers for different data types
    @cast_spell.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @cast_spell.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @cast_spell.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return cast_spell


if __name__ == "__main__":
    print("Testing spell reducer...")
    test_spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(test_spells, 'add')}")
    print(f"Product: {spell_reducer(test_spells, 'multiply')}")
    print(f"Max: {spell_reducer(test_spells, 'max')}")

    # def sample_enchant(power: int, element: str, target: str) -> str:
    #     return f"Cast {element} on {target} with {power} power"
    # enchanters = partial_enchanter(sample_enchant)
    # print(enchanters['fire']("Goblin"))
    # print(enchanters['fire']("Wizard"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    # kima f subject verifying caching works
    # print(memoized_fibonacci.cache_info())

    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    print(dispatch(["fireball", "heal", "shield"]))
    print(dispatch(3.14))
