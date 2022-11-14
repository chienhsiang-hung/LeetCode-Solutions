# first record the times in a dict
# then return them in the required order

from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = defaultdict(lambda: [0, ''])
        for word in words:
            word_count[word][0] -= 1
            word_count[word][1] = word
        word_count = list(word_count.values())
        heapq.heapify(word_count)
        return [
            item[1] for item in heapq.nsmallest(k, word_count)
        ]

        