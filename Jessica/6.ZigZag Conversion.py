class Solution:
    def convert(self, s: str, numRows: int) -> str:
        length=len(s)
        if length <=numRows:
            return s
        if numRows==1:
            return s
        count=numRows+(numRows-2)
        groups=int(length/count)+1
        Outter = []
        for i in range(0,groups):
            Inner=[]
            Inner=list(s[i*count:i*count+count])            
            Outter.append(Inner)

        while len(Outter[groups-1])<count:
            Outter[groups-1].append('@')
        ret = ''

        for i in range(0,groups):
            for j in range(1,numRows-1):
                Outter[i][j] = Outter[i][j] + Outter[i][count-j]  
            for k in range(0,count-numRows):
                Outter[i].pop()
        for j in range(0,numRows):
            for i in range(0,groups):            
                ret+=Outter[i][j]
        return ret.replace('@','')
