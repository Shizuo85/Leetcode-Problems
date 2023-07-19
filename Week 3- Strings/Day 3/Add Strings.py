class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1)<len(num2): num1,num2 = num2,num1
        num2 = "0"*(len(num1) - len(num2)) + num2
        
        carry=0
        ans=""
        
        for i in range(len(num1)-1, -1, -1):
            curr = int(num1[i])+int(num2[i])+carry   
            carry = curr//10
            curr = curr%10
            
            ans = str(curr) + ans
        if carry:
            ans = "1" + ans
        return ans