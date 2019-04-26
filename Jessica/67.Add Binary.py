class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c=int(a)+int(b)
        StrC='0'+str(c)
        ret=''
        carry=0
        for i in range(len(StrC)-1,-1,-1):
            if StrC[i]=='2' and carry==0:
                ret+='0'
                carry=1
            elif StrC[i]=='2' and carry==1:
                ret+='1'
                carry=1
            elif StrC[i]=='0' and carry==0:
                ret+=str(0)
            elif StrC[i]=='0' and carry==1:
                ret+='1'
                carry=0
            elif StrC[i]=='1' and carry==0:
                ret+='1'
            elif StrC[i]=='1' and carry==1:
                ret+='0'
                carry=1
        if ret[len(ret)-1]=='0':
            ret=ret[:len(ret)-1]        
        return ret[::-1]
            
