class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper().replace("-", "")
        ans  = s[:len(s)%k]
        right = s[len(s)%k:]
        for i in range(0, len(right), k):
            ans = ans+"-"+right[i:i+k]
        return ans if not ans or ans[0]!="-" else ans[1:]