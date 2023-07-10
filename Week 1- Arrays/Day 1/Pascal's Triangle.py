class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        lst =[[1]]
        for i in range(numRows-1):
            add=[]
            for m in range(len(lst[i])-1):
                add+=[lst[i][m]+lst[i][m+1]]
            lst.append([1] + add + [1])
        return lst