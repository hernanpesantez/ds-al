import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        for i in range(len(s)):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True


res = Solution().isPalindrome("A man, a plan, a scanal: Panama")
print(res)
