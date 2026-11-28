class TimeMap:
    def __init__(self):
        self.mp = collections.defaultdict(lambda : {})     

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key][timestamp] = value 

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp : return ''
        if timestamp not in self.mp[key]:
            for i in range(timestamp - 1, -1, -1):
                if i in self.mp[key]:
                    return self.mp[key][i]
            return ''
        return self.mp[key][timestamp]
