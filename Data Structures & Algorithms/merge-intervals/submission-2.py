class Solution:
    def merge(self, A: List[List[int]]) -> List[List[int]]:
        A.sort()
        cur = A[0]; ans = []
        for new in A[1:]:
            if new[0] > cur[1]:
                ans.append(cur)
                cur = new
            else:
                cur[1] = max(new[1], cur[1])
        return ans + [cur]