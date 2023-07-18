class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels ={"a","e","i","o","u","A","E","I","O","U"}
        i=0
        j=len(s)-1
        s=list(s)
        
        while i<j:
            if s[i] not in vowels:
                i+=1
            if s[j] not in vowels:
                j-=1
            if s[i] in vowels and s[j] in vowels:
                s[i], s[j] = s[j], s[i]
                i+=1
                j-=1

        return "".join(s)