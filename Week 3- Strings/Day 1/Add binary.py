class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a)<len(b):
            a,b =b,a
        b = "0"*(len(a)-len(b)) + b
        ans= ""
        carry=0
        for i in range(-1, -len(a)-1, -1):
            x = int(a[i])+int(b[i])+carry
            carry = x//2
            x=x%2
            
            ans = str(x) + ans
        if carry:
            ans ="1" +ans
        return ans
        
            