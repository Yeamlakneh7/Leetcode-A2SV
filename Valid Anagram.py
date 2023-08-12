class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        word1 = sorted(s)
        word2 = sorted(t)
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                return False
        return True
