class Solution:
    def scoreOfString(self, s: str) -> int:
        
        sumascii = 0
        for i in range(len(s)-1,0,-1):
            sumascii += abs(ord(s[i])-ord(s[i-1]))

        return sumascii

        