class Solution:
    def searchMatrix(self, grid: List[List[int]], target: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        
        def binary_search(arr, target):
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1

            return False

        for r in range(rows):
            if binary_search(grid[r], target):
                return True
        return False