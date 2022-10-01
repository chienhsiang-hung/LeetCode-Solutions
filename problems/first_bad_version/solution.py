# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        _mid = (left + right) //2

        # handle the only one bad in a length-1 array
        if n == 1 and isBadVersion(1):
            return 1

        while left<=right:
            # Good
            if isBadVersion(_mid) is False:
                if isBadVersion(_mid+1):
                    return _mid+1
                left = _mid +1
                _mid = (left + right) //2

            # Bad
            else:
                if isBadVersion(_mid-1) is False:
                    return _mid
                right = _mid -1
                _mid = (left + right) //2
        return -1