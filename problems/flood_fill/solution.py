# BFS

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        pixel_q =[(sr, sc)]
        height = len(image)
        length = len(image[0])

        colored = []
        for i in range(height):
            colored.append([])
            for j in range(length):
                colored[i].append(False)

        target_p = image[sr][sc]
        if target_p == color:
            return image

        while pixel_q:
            current = pixel_q.pop(0)
            sr = current[0]
            sc = current[1]
            colored[sr][sc] = True

            if image[sr][sc] == target_p:
                image[sr][sc] = color

            # top 
            if sr -1 >= 0:
                if colored[sr-1][sc] is False and image[sr-1][sc] == target_p:
                    pixel_q.append((sr-1, sc))
            # right
            if sc +1 <= length-1:
                if colored[sr][sc+1] is False and image[sr][sc+1] == target_p:
                    pixel_q.append((sr, sc+1))
            # bottom
            if sr +1 <= height-1:
                if colored[sr+1][sc] is False and image[sr+1][sc] == target_p:
                    pixel_q.append((sr+1, sc))
            # left
            if sc -1 >= 0:
                if colored[sr][sc-1] is False and image[sr][sc-1] == target_p:
                    pixel_q.append((sr, sc-1))
        return image