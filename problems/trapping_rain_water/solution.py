# [0,1,0,2,1,0,1,3,2,1,2,1]
# 0, 1
# 1, 0 <- 1 is left
# 0, 2 <- (1,1)to(2,3) add=1
# 2, 1 <- 2 is left
# 1, 0 add=1
# 0, 1 add=2
# 1, 3 <- (2,3)to(3,7) add=1
# 3, 2 <- 3 is left
# 2, 1 add=1
# 1, 2 add=2
# 2, 1 ...

class Solution:
    def trap(self, height: List[int]) -> int:
        i = -1
        left = None
        current_window = []
        output = 0

        if len(height) < 2:
            return output

        while i < len(height)-2:
            i += 1

            # find the left wall
            if left is None and height[i] > height[i+1]:
                left = i
                continue
            # find the right wall
            if left != None and height[left] <= height[i]:
                output += sum(current_window)
                # reset temps
                current_window = []
                left = i if height[i] > height[i+1] else None
                continue
            
            if left != None:
                current_window.append(height[left]-height[i])

        i += 1
        # check for deadend
        if left != None:
            if height[left] <= height[i]:
                output += sum(current_window)
            else:
                i += 1
                # try to find the right (from right to left repeat the same thing)
                right = None
                current_window = []
                while i-1 >= left:
                    i -= 1
                    # find the right wall
                    if right is None and height[i] > height[i-1]:
                        right = i
                        continue

                    # find the left wall
                    if right != None and height[right] <= height[i]:
                        output += sum(current_window)
                        # reset temps
                        current_window = []
                        right = i if height[i] > height[i-1] else None
                        continue
                    
                    if right != None:
                        current_window.append(height[right]-height[i])

        return output
