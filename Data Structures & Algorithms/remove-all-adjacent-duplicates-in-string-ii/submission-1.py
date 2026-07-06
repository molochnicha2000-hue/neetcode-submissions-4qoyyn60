class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        N = len(s) 
        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
            
            if stack and stack[-1][1] == k:
                stack.pop()

        res = ""
        for char, times in stack:
            res += char * times
        return res

