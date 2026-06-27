class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        N = len(weights)
        store = []
        for i in range(N - 1):
            store.append(weights[i] + weights[i + 1])

        store.sort()
        k -= 1
        c = weights[0] + weights[-1]
        M1 = c + sum(store[-k : ])
        M2 = c + sum(store[:k])
        return M1 - M2