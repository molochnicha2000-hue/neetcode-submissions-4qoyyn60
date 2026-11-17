class LRUCache:
    def __init__(self, sz: int):
        self.sz = sz
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache : return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.sz:
            self.cache.popitem(last = False)

        