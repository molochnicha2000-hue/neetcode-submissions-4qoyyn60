class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort(key = lambda y: (abs(y- x), y))
        
        return sorted(arr[:k])
        