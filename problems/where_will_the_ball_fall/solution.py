class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        answer = [-1] * len(grid[0])
        routes = []
        # check the entries
        for c in range( len(grid[0]) -1 ):
            if grid[0][c] == grid[0][c+1] == 1:
                routes.append({
                    'row': 1,
                    'c': c,
                    'answer_pos': c,
                    'dir': 1   
                })
            elif grid[0][c] == grid[0][c+1] == -1:
                routes.append({
                    'row': 1,
                    'c': c,
                    'answer_pos': c+1,
                    'dir': -1  
                })

        # check the following routes
        for r in range( 1, len(grid) ):

            while routes:
                if routes[0]['row'] != r:
                    break

                current = routes.pop(0)

                c = current['c']
                answer_pos = current['answer_pos']
                _dir = current['dir']

                # record the right path
                if _dir == 1:
                    if c+2 <= len(grid[0])-1:
                        # go right
                        if grid[r][c+1] == grid[r][c+2] == 1:
                            routes.append({
                                'row': r+1,
                                'c': c+1,
                                'answer_pos': answer_pos,
                                'dir': 1   
                            })
                            continue
                    # go left
                    if grid[r][c] == grid[r][c+1] == -1:
                        routes.append({
                            'row': r+1,
                            'c': c,
                            'answer_pos': answer_pos,
                            'dir': -1
                        })
                # record the left path
                else:
                    if c-1 >= 0:
                        # go left
                        if grid[r][c] == grid[r][c-1] == -1:
                            routes.append({
                                'row': r+1,
                                'c': c-1,
                                'answer_pos': answer_pos,
                                'dir': -1   
                            })
                            continue
                    # go right
                    if grid[r][c] == grid[r][c+1] == 1:
                        routes.append({
                            'row': r+1,
                            'c': c,
                            'answer_pos': answer_pos,
                            'dir': 1
                        })
        for route in routes:
            if route['dir'] == 1:
                answer[ route['answer_pos'] ] = route['c']+1
            else:
                answer[ route['answer_pos'] ] = route['c']

        return answer