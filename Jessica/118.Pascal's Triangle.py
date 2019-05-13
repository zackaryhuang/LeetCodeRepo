class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        else:
            outter=[[1]]
            for i in range(1,numRows):
                inner=[1]
                for j in range(1,i):
                    inner.append(outter[i-1][j-1]+outter[i-1][j])
                inner.append(1)
                outter.append(inner)    
        return outter
        
