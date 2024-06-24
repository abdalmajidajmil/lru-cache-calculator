"""
file to check  our implementations of classes and methods
"""
from cache_calculator import CacheCalculator
from lru_cache import LruCache


def main():
    cache1 = LruCache(3)
    cache1.put(key=[1, 2], value=0)
    cache1.put(key={3, 4}, value=1)
    cache1.put(key={1: 2, 3: 4}, value=2)
    print(cache1)

    my_calculator1 = CacheCalculator(size=3)
    result, from_cache = my_calculator1.calculate(left_side=4, right_side=3, operator='sum')
    print(f"Result: {result}, From cache: {from_cache}")

    result, from_cache = my_calculator1.calculate(left_side=4, right_side=3, operator='sum')
    print(f"Result: {result}, From cache: {from_cache}")

    result, from_cache = my_calculator1.calculate(left_side=5, right_side=2, operator='mul')
    print(f"Result: {result}, From cache: {from_cache}")

    result, from_cache = my_calculator1.calculate(left_side=2, right_side=5, operator="sum")
    print(f"Result: {result}, From cache: {from_cache}")

    result, from_cache = my_calculator1.calculate(left_side=5, right_side=2, operator='sum')
    print(f"Result: {result}, From cache: {from_cache}")

    print("-" * 50)

    my_calculator2 = CacheCalculator(size=1)
    result, from_cache = my_calculator2.calculate(left_side=2, right_side=5, operator='sum')
    print(f"Result: {result}, From cache: {from_cache}")

    result, from_cache = my_calculator2.calculate(left_side=3, right_side=1, operator='mul')
    print(f"Result: {result}, From cache: {from_cache}")

    result, from_cache = my_calculator2.calculate(left_side=1, right_side=3, operator='mul')
    print(f"Result: {result}, From cache: {from_cache}")

    print("-" * 50)

    my_calculator2 = CacheCalculator(size=4)
    result, from_cache = my_calculator2.calculate(left_side=0, right_side=0, operator='mul')
    print(f"Result: {result}, From cache: {from_cache}")

    result, from_cache = my_calculator2.calculate(left_side=2, right_side=1, operator='mul')
    print(f"Result: {result}, From cache: {from_cache}")

    result, from_cache = my_calculator2.calculate(left_side=100, right_side=3, operator='sub')
    print(f"Result: {result}, From cache: {from_cache}")

    result, from_cache = my_calculator2.calculate(left_side=10, right_side=4, operator='mul')
    print(f"Result: {result}, From cache: {from_cache}")

    result, from_cache = my_calculator2.calculate(left_side=2, right_side=1, operator='mul')
    print(f"Result: {result}, From cache: {from_cache}")

    result, from_cache = my_calculator2.calculate(left_side=11, right_side=2, operator='mul')
    print(f"Result: {result}, From cache: {from_cache}")

    result, from_cache = my_calculator2.calculate(left_side=0, right_side=0, operator='mul')
    print(f"Result: {result}, From cache: {from_cache}")


if __name__ == "__main__":
    main()
