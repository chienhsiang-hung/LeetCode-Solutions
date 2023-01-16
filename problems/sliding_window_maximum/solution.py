class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        indices = deque() # keep track on their indices to maintain the window (popleft)
        output = []

        for i, n in enumerate(nums):
            # use bigger num to replace the small num, the valume order will be decreasing
            while indices and n > nums[indices[-1]]:
                indices.pop()

            indices.append(i)

            # maintain the size of window
            if indices[0] == i-k:
                indices.popleft()
            
            if i >= k-1:
                output.append(nums[indices[0]]) # because the valume order will be decreasing
        
        return output