class Stack:
    def __init__(self, maxLength: int = 10) -> None:
        self.items = []
        self.maxLength = maxLength
    
    def add(self, item) -> dict:
        self.items.append(str(item))
        result = {
            "state": False,
            "data": None
        }
        if len(self.items) >= self.maxLength:
            result["data"] = self.toString()
            result["state"] = True

        return result

    def toString(self) -> str:
        result = '\n'.join(self.items)
        print(result)
        self.items = []
        return result