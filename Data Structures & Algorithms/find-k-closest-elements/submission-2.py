import bisect
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        N = len(arr)
        index = 0
        for i in range(1, N):
            if abs(x - arr[index]) > abs(x - arr[i]):
                index = i

        res = [arr[index]]

        l, r = index - 1, index + 1
        while len(res) != k:
            if l >= 0 and r < N:
                if abs(arr[l] - x) <= abs(arr[r] - x):
                    res.append(arr[l])
                    l -= 1
                else:
                    res.append(arr[r])
                    r += 1

            elif l >= 0:
                res.append(arr[l])
                l -= 1
            elif r < N:
                res.append(arr[r])
                r += 1

        return sorted(res)