class Solution(object):
    def plusOne(self, digits):
      return list(map(int, list(str(int("".join(map(str, digits))) + 1))))


#OR

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0

        return [1] + digits 


