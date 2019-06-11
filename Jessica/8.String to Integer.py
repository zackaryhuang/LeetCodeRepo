class Solution:
    def myAtoi(self, str: str) -> int:
        if len(str)==0:
            return 0
        if len(str.replace(' ',''))==0:
            return 0
        list1=list(str)        
        is_char='+-0123456789'
        is_num='0123456789'
        is_flag='+-'        
        temp=''
        flag='+'
        if len(str)==1 and str not in is_num:
            return 0
        for i in range(0,len(list1)):
            
            if list1[i] ==' ' and len(temp)==0:
                continue
            elif len(temp)==0 and list1[i] not in is_char:
                return 0
            
            elif len(temp)==0 and list1[i] in is_flag and list1[i+1] not in is_num:
                return 0
            elif len(temp)==0 and list1[i] in is_flag and list1[i+1] in is_num:
                flag=list1[i]
            elif list1[i] not in is_num and len(temp)>0:
                break            
            else:
                temp+=list1[i]     
        
        ret=int(temp)
       
        if flag=='-':
            ret=ret*-1            
        if ret>=-2147483648 and ret<=2147483647: 
            return ret
        elif ret<-2147483648:
            return -2147483648
        elif ret>2147483647: 
            return 2147483647
        
