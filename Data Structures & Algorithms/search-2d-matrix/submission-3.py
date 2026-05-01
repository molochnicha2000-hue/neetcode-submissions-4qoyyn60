class Solution:
    def searchMatrix(self, grid: List[List[int]], target: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        top, bot = 0, rows - 1

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

        while top <= bot:
            row = (top + bot) // 2
            if target > grid[row][-1]:
                top = row + 1
            elif target < grid[row][0]:
                bot = row - 1
            else:
                break
        #print(row)
        
        return binary_search(grid[row], target)