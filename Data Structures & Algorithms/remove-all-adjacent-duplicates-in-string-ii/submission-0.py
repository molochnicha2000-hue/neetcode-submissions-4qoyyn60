class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        N = len(s)
        if k > N:
            return s
        
        stack = []
        def good(need):
            count = 1
            for i in range(len(stack) - 1, -1, -1):
                if stack[i] != need:
                    return count == k
                count += 1
                if count == k:
                    return True


        count = 0
        for i in range(N):
            if len(stack) >= k - 1 and good(s[i]):
                
                tries = 0
                while stack and tries != k - 1:
                    stack.pop()
                    tries += 1
            else:
                stack.append(s[i])
        return "".join(stack)

