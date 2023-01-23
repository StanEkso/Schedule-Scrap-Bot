class IntegerHash:
    """
    Hash table for storing integer values by string keys
    """
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
        return self.table.get(key)

    def has(self, key: str) -> bool:
        return key in self.table
