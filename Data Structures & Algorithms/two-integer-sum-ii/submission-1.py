class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        #right = 1
        r = len(numbers) - 1
        numbers.sort()

        while l < r:
            summa = numbers[l] + numbers[r]
            if l < r and numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            
            if summa > target:
                r -= 1
            else:
                l += 1
        
        