# Using stack approach

class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_stack = []
        delete_cnt = 0

        for char in s:
            if char_stack and char_stack[-1] == "b" and char == "a":
                char_stack.pop()
                delete_cnt += 1
            else:
                char_stack.append(char)

        return delete_cnt
        
