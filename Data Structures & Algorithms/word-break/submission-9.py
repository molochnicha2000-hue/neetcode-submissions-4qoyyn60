class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(wordDict)
        targetLen = len(s)
        dp = [False] * (targetLen + 1)
        dp[targetLen] = True

        for i in range(targetLen - 1, -1, -1):
            #cur_dp = dp[i]
            for j in range(N):
                curLen = len(wordDict[j])
                if i + curLen <= targetLen and s[i : i + curLen] == wordDict[j]: 
                    dp[i] = dp[i + curLen]
                    #if dp[i + curLen]:
                        #dp[i] = dp[i + curLen]
                if dp[i]:
                    break
        #print(dp)
        return dp[0]