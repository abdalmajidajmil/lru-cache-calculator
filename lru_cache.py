from typing import Any


class LruCache:

    def __init__(self, size: int):
        """

        :type size: object
        """
        self.size = size
        self.cache = {}

    def put(self, key: Any, value: Any):
        self.cache[key] = value

    def get(self, key: Any) -> Any:
        if key not in self.cache:
            return None
        else:
            return self.cache[key]

    def __hash__(self):
        ins_hash = (self.cache,)
        return hash(ins_hash)

    def __str__(self):
        s_cache: str = ""
        for key, value in self.cache.items():
            s_cache += f"{key} : {value}\n"

        return s_cache
