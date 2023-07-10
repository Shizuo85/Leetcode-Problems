class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        lst =[1]

        for i in range(rowIndex):
            add=[]

            for m in range(len(lst)-1):

                add+=[lst[m]+lst[m+1]]

            lst=[1] + add + [1]

        return lst