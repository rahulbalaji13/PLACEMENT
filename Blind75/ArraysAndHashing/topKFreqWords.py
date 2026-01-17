from collections import Counter
import heapq

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = Counter(words)

        words_sorted = sorted(count.keys(), key = lambda word : (-count[word], word))

        return words_sorted[:k]
        
