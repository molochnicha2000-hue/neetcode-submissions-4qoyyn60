class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        N = len(arr)
        res = 0
        total = sum(arr[:k])
        if total / k >= threshold:
            res += 1

        
        for i in range(k, N):
            total += arr[i]
            total -= arr[i - k]
            if total / k >= threshold:
                res += 1
            
        return res