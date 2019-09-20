class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        else:
            outter=[[1]]
            for i in range(1,rowIndex+1):
                inner=[1]
                for j in range(1,i):
                    inner.append(outter[i-1][j-1]+outter[i-1][j])
                inner.append(1)
                outter.append(inner)    
        return outter[rowIndex]

