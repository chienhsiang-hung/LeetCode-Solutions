# Let's run the programme together
# abcbbcbb

# a 1
# ab 2
# abc 3
# abcb -> bcb -> cb 2
# cbb -> bb -> b 1
# bc 2
# bcb -> cb 2
# ...


from collections import defaultdict, deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_map = defaultdict(int)
        word_q = deque([])

        output = 0        
        for ch in s:
            window_map[ch] += 1
            word_q.append(ch)
            while window_map[ch] > 1:
                window_map[word_q.popleft()] -= 1
            output = max(output, len(word_q))
        return output
                
            