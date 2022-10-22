from typing import Generic, TypeVar

T = TypeVar("T")
K = TypeVar("K")


class Hash(Generic[T, K]):
    table: dict[T, K]

    def __init__(self) -> None:
        super().__init__()
        self = self
        pass

    def set(self, key: T, value: K) -> bool:
        try:
            self.table[key] = value
            return True
        except:
            return False

    def get(self, key: T) -> K:
        return self.table.get(key)


class IntegerHash:
    table: dict[str, int] = dict()

    def __init__(self) -> None:
        pass

    def set(self, key: str, value: int) -> bool:
        try:
            self.table[key] = value
            return True
        except:
            return False

    def get(self, key: str) -> int:
        return self.table.get(key) or 0
