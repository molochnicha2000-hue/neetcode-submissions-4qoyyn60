class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''
        res = []
        for x in strs:
            res.append(str(len(x)))
            res.append('#')
            res.append(x)
        return ''.join(res)

    def decode(self, s : str) -> List[str]:
        if not s:
            return []
        i = 0
        res = []
        while i < len(s):
            j = i
            while j < len(s) and s[j] != '#':
                j += 1
            length = int(s[i : j])
            i = j + 1
            res.append(s[i : i + length])
            i = j + 1 + length
        return res
