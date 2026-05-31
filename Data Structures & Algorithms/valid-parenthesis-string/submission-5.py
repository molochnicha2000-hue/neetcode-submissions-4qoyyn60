class Solution:
    def checkValidString(self, s: str) -> bool:
        mi, ma = 0, 0
        for c in s:
            if c == "(":
                mi, ma = mi + 1, ma + 1
            elif c == ")":
                mi -= 1
                ma -= 1
            else:
                mi -= 1
                ma += 1
            if ma < 0:
                return False
            mi = max(0, mi)
        return mi == 0