class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        '''
        count the "joint" intervals
        [[10,16],[2,8],[1,6],[7,12]]
        -> [[1,6], [2,8], [7,12], [10,16]]
        [[1,6]]
        [[2,6]]
        [[2,6], [7,12]]
        [[2,6], [10,12]]
        '''
        points.sort()

        new_points = [points[0]]
        for i in range(1, len(points)):
            if new_points[-1][0] <= points[i][0] <= new_points[-1][1]:
                new_points[-1] = [
                    max(new_points[-1][0], points[i][0]),
                    min(new_points[-1][1], points[i][1])
                ]
            else:
                new_points.append(points[i])
        return len(new_points)
