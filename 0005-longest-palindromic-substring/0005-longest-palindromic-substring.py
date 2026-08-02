class Solution:
    def longestPalindrome(self, s: str) -> str:
        le = 0
        st = ""
        for h in range(len(s)):
            for a in range(h,len(s)+1):
                ah = s[h:a]
                if ah == ah[::-1]:
                    if len(ah) >= le:
                        le = len(ah)
                        st = ah

        return st

