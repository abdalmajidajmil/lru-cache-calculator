# lru-cache-calculator

The LRU Cache Calculator Python project combines an LRU Cache with an arithmetic calculator.

## Features

- **LRU Cache Implementation**: A custom LRU cache that stores results of arithmetic operations. The cache has a fixed size and automatically evicts the least recently used items when it reaches capacity.
- **Arithmetic Operations**: Supports basic arithmetic operations including addition, subtraction, multiplication, and division.
- **Operator Management**: Utilizes Python's `enum` module to handle arithmetic operators in a structured and organized manner.
- **Cache Utilization**: Reduces computation time by retrieving results from the cache for repeated operations.

## Modules

- **`lru_cache.py`**: Implements the LRU cache with methods to add, retrieve, and manage cache entries.
- **`cache_calculator.py`**: Contains the `CacheCalculator` class that integrates the LRU cache with arithmetic operations. Also includes the `Calculation` class to perform the operations.
- **`Main.py`**: Provides test cases and demonstrations of the LRU cache and calculator functionalities.
