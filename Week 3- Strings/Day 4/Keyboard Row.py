class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set1 = set("qwertyuiop")
        set2 = set("asdfghjkl")
        set3 = set("zxcvbnm")
        
        ans = []
        for i in words:
            x=i.lower()
            if set1&set(x)==set(x) or set2&set(x)==set(x) or set3&set(x)==set(x):
                ans.append(i)
        return ans