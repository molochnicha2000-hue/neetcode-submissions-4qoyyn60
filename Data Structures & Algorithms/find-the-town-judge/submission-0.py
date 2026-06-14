class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adg = {i : set() for i in range(1, n + 1)}
        for ai, bi in trust:
            adg[ai].add(bi)
            

        
        for person, trusts in adg.items():
            if len(trusts) != 0:
                continue
        
            flag = True
            for per in range(1, n + 1):
                if per == person:
                    continue
                if person not in adg[per]:
                    flag = False
                    break
                
            if flag:
                return person
        return -1
        """
        1 - [3]
        2 - [3]
        3 - []

        """