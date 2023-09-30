class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for i in s:
            if i.isalnum():
                st += i
        st = st.lower()
        if len(st) <= 1:
            return True
        l = 0
        r = len(st) - 1
        while l < r:
            if st[l] != st[r]:
                return False
            r -= 1    
            l += 1
        return True
