class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            # Convert the integer to a string and compare it with its reverse
            s = str(x)
            return s == s[::-1]
