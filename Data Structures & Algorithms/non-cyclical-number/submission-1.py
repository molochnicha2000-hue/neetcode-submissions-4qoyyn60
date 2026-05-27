class Solution:
    def isHappy(self, n: int) -> bool:
        def new_num(cur):
            new_n = 0
            for i in str(cur):
                new_n += int(i) ** 2
            return new_n

        def good(n):
            new_n = 0
            for i in str(n):
                new_n += int(i) ** 2
            if new_n == n:
                return True
            return False
        visited = set()
        
        cur = n
        while cur not in visited:
            print(cur)
            if good(cur):
                return True
            visited.add(cur)
            cur = new_num(cur)
        return False


        