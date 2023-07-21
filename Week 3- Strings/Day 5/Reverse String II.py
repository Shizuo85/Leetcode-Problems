class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans =""
        prev=0
        for i in range(0, len(s), 2*k):
            ans= ans+s[prev:i] + s[i:i+k][::-1]
            prev = i+k
        return ans + s[prev:]