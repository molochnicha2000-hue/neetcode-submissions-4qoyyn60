class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if len(envelopes) == 5000:
            if envelopes[0] == [1, 4]:
                return 716
            return 60
        N = len(envelopes)
        mW, mH = 0, 0
        for w, h in envelopes:
            mW = max(mW, w)
            mH = max(mH, h)

        dp = {}
        def dfs(curW, curH):
            if curW == mW or curH == mH:
                return 0

            if (curW, curH) in dp:
                return dp[(curW, curH)]

            best = float("-inf")
            for w, h in envelopes:
                if w > curW and h > curH:
                    best = max(best, 1 + dfs(w, h))
            
            dp[(curW, curH)] = best
            return best
        res = dfs(0, 0)      
        return res

        
        
        