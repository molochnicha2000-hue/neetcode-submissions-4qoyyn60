class Solution:
    def isValid(self, s: str) -> bool:
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