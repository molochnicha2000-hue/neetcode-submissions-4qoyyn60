class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1: return False
        if s[0] in ")}]": return False
        if s[-1] in "[{(": return False
        stack = []
        must_be = {"]":"[",
                    "}":"{",
                    ")":"("}
        
        for c in s:
            if c in must_be:
                if stack and stack[-1] == must_be[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False