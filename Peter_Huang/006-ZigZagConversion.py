class Solution:
    def convert(self, s: str, numRows: int) -> str:
        return func(s,numRows)
def func(str, numRows):
    result = []
    for i in range(0,numRows):
        result.append([])
    j = 0
    m = 0
    flag = 0
    while(m < len(str)):
        if j < numRows:
            result[j].append(str[m])
        else:
            result[numRows-1].append(str[m])
        if j == numRows-1:
            flag = 1
        if j == 0:
            flag = 0
        if flag == 0:
            j+=1
        if flag == 1:
            j-=1
        m+=1
    str = ''
    for list in result:
        for char in list:
            str+=char
    return str