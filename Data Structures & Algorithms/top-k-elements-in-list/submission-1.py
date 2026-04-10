class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = [[] for _ in range(len(nums) + 1)]
        nums.sort()

        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, t in count.items():
            res[t].append(n)

        answer = []
        for i in range(len(res) - 1, -1, -1):
            for n in res[i]:
                answer.append(n)
                if len(answer) == k:
                    return answer

        #return answer
            
        