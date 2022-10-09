class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        _list = []
        row = 0
        column = 0
        _dir = 'right'
        
        right_bound = len(matrix[0])-1
        bottom = len(matrix)-1
        left_bound = 0
        top = 1

        while matrix[row][column] is not None:
            _list.append(matrix[row][column])
            matrix[row][column] = None
            if _dir == 'right' and column == right_bound: # hit the right bound
                _dir = 'down'
                right_bound -= 1
            elif _dir == 'down' and row == bottom:
                _dir = 'left'
                bottom -= 1
            elif _dir == 'left' and column == left_bound:
                _dir = 'up'
                left_bound += 1
            elif _dir == 'up' and row == top:
                _dir = 'right'
                top += 1

            if _dir == 'right':
                column += 1
            elif _dir == 'down':
                row += 1
            elif _dir == 'left':
                column -= 1
            elif _dir == 'up':
                row -= 1
                
            if column >= len(matrix[0]) or row >= len(matrix):
                break
        return _list
            