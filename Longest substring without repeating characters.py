class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        a = 0
        set1 = set()
        for b in range(len(s)):
            while s[b] in set1:
                set1.remove(s[a])
                a = a + 1
            set1.add(s[b])
            longest = max(longest, b - a + 1)
        return longest

        
