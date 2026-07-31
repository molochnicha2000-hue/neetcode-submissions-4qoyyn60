class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        need = collections.Counter(s1)

        def good(current):
            for char, freq in need.items():
                if current[char] != freq:
                    return False       
            for char, freq in current.items():
                if need[char] != freq:
                    return False
            return True

        for l in range(n):
            f = collections.Counter()
            for r in range(l,n):
                f[s2[r]] += 1
                if good(f):
                    return True
        return False


        