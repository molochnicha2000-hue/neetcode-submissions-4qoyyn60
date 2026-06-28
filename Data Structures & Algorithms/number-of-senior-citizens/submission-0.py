class Solution:
    def countSeniors(self, details: List[str]) -> int:
        N = len(details)
        res = 0

        for cur in details:
            age = int(cur[11 : 13])
            if age > 60:
                res += 1
        return res