class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        countS1 = {}
        for c in s1:
            countS1[c] = 1 + countS1.get(c, 0)

        need = len(countS1)
        for i in range(len(s2)):
            hashT, eq = {}, 0
            for j in range(i, len(s2)):
                hashT[s2[j]] = 1 + hashT.get(s2[j], 0)

                if countS1.get(s2[j], 0) < hashT[s2[j]]:
                    break
                

                if countS1.get(s2[j]) == hashT[s2[j]]:
                    eq += 1
                if eq == need:
                    return True
            
        return False
 
        