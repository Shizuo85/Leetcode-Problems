class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n=0
        if not s:
            return True
        for i in t:
            if i == s[n]:
                n+=1
                if n==len(s):
                    return True
            
        return False