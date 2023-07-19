class Solution:
    def longestPalindrome(self, s: str) -> int:
        s = Counter(s)
        even = 0
        odd = 0
        seenOdd=False
        
        for i in s:
            if s[i]%2==0:
                even+=s[i]
            else:
                if s[i]>1:
                    odd+=s[i]-1
                seenOdd=True

        if seenOdd:odd+=1
            
        return odd + even