class Solution:
    def countSegments(self, s: str) -> int:
#       return len(s.split())
        ans = 0
        char = False
        for i in s:
            if i != " " and not char:
                char = True
                ans+=1
            elif i == " " and char:
                char = False
        return ans           