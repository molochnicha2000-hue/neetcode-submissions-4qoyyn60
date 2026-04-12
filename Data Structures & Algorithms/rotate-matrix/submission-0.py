class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        
        while l < r:
            for i in range(r - l):
                top, bot = l, r

                tempLeft = matrix[top][l + i]

                # move bottom left to top left
                matrix[top][l + i] = matrix[bot - i][l]

                # move bottom right to bottom left
                matrix[bot - i][l] = matrix[bot][r - i]

                # move top right to bottom right
                matrix[bot][r - i] = matrix[top + i][r]

                # move top left to top right
                matrix[top + i][r] = tempLeft
            r -= 1
            l += 1
        

        


        