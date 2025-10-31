'''
2x2->1 (1)
3x3->2 (2)
4x4->5 ([2x2]+3)=(1+3)=4
5x5->7 ([3x3]+4)=(2+4)=6
6x6-> ([4x4]+5)=(4+5)=9
7x7-> ([5x5]+6)=(6+6)=12
8x8-> ([6x6]+7)=(9+7)=16
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 1: return


        for r in range(int(len(matrix)//2)):
            for c in range(r, len(matrix)-1-r):
                matrix[r][c], matrix[c][len(matrix)-1-r], matrix[len(matrix)-1-r][len(matrix[0])-1-c], matrix[len(matrix)-1-c][r] = matrix[len(matrix)-1-c][r], matrix[r][c], matrix[c][len(matrix)-1-r], matrix[len(matrix)-1-r][len(matrix[0])-1-c]
        
