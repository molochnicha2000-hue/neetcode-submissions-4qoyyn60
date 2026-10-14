from collections import defaultdict
class TimeMap:
    def __init__(self):
        self.storage = defaultdict(lambda : {})

    def set(self, key: str, value: str, time: int) -> None:
        self.storage[key][time] = value

    def get(self, key: str, time: int) -> str:
        if key not in self.storage:
            return ''
        if time not in self.storage[key]:
            for i in range(time - 1, -1, -1):
                if i in self.storage[key]:
                    return self.storage[key][i]
            return ''
        return self.storage[key][time]
