class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        _mid = (left + right) //2            

        while 0 <= _mid <= len(nums)-1 and left <= right:
            if target == nums[_mid]:
                return _mid
            
            if target < nums[_mid]:
                right = _mid -1
                _mid = (left + right) // 2
            else:
                left = _mid +1
                _mid = (left + right) // 2
                
        return -1