class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        return letters[bisect_right(letters, target) % len(letters)]

  # biect_right() -> Used to do binary search by maintaing sorted arrays
