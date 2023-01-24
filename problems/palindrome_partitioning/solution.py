# https://leetcode.com/problems/palindrome-partitioning/solutions/1667786/python-simple-recursion-detailed-explanation-easy-to-understand/
# https://www.youtube.com/watch?v=0_ievUF0L_E

class Solution:
    @cache
    def partition(self, s: str) -> List[List[str]]:
        if not s: return [[]]

        ans = []
        for i in range(1, len(s)+1):
            if s[:i] == s[:i][::-1]: # check palindrome
                for solution in self.partition(s[i:]):
                    ans.append(
                        [s[:i]] + solution
                    )

        return ans