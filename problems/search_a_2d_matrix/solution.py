# efficient algorithm: Binary Search

# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# 3
#########################################
# width = 4, height=3
# mid = 5, current = matrix[1][1] = 11
# mid = (0+4)//2 = 2, current = matrix[0][2] = 5
# mid = (0+1)//2 = 0, current = matrix[0][0] = 1
# mid = (1+1)//2 = 1, current = matrix[0][1] = 3
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        width = len(matrix[0])
        height = len(matrix)
        n_items = width * height
        
        left, right = 0, n_items-1
        while left <= right:
            mid = (left + right) // 2
            ######
            current = matrix[mid//width][mid%width]
            ######
            if current == target:
                return True
            elif current < target:
                left = mid+1
            else:
                right = mid-1
        return False