class TimeMap:
    #              1       2        3
    # alice -> ["happy", "sad", "boring"]
    def __init__(self):
        self.storage = collections.defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key][timestamp] = value 

    def get(self, key: str, timestamp: int) -> str:
        # there is not key
        if not key in self.storage:
            return ""   
        
        # if not less timestamp than cur timestamp before: return ""
        """
        if not timestamp in self.storage[key]:
            flag = False
            for i in range(timestamp, 1000, 1):
                if self.storage[key][tim]
    
        if flag:
            return ""
        """
        flag = False
        # search in key timestamp
        if timestamp not in self.storage[key]:
            for i in range(timestamp - 1 , 0, -1):
                if i in self.storage[key]:
                    return self.storage[key][i]
            flag = True
        if flag:
            return ""
        # basekey
        return self.storage[key][timestamp]
