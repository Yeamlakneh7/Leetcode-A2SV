class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s))
        j = -1
        value = 0
        for i in s.lower():
            if i != s.lower()[j]:
                value = 1
                break
            j = j - 1
        if value == 1:
            return False
        else:
            return True
