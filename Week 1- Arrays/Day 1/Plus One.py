class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1, -1, -1):
            if digits[i]==9:
                digits[i]=0
                if i-1<0:
                    digits= [1] + digits 
            else:
                digits[i] +=1
                break
        return digits 