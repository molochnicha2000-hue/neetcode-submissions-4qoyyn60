class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        M = max(len(word1), len(word2))
        N = min(len(word1), len(word2))
        last = 0
        for i in range(N):
            res += word1[i] 
            res += word2[i]
            last = i
        
        if M - N != 0:
            need = None
            if len(word1) > len(word2):
                need = word1
            else:
                need = word2
            
            res += need[last + 1: M]
        return res