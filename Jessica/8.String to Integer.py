class Solution:
    def myAtoi(self, str: str) -> int:
        if len(str)==0:
            return 0
        if len(str.replace(' ',''))==0:
            return 0
        list1=list(str)        
        ascii2integer={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        is_char='+-0123456789'
        is_num='0123456789'
        is_flag='+-'
        list2=[]
        temp=''
        flag='+'
        if len(str)==1 and str not in is_num:
            return 0
        for i in range(0,len(list1)):
            
            if list1[i] ==' ' and len(list2)==0:
                continue
            elif len(list2)==0 and list1[i] not in is_char:
                return 0
            
            elif len(list2)==0 and list1[i] in is_flag and list1[i+1] not in is_num:
                return 0
            elif len(list2)==0 and list1[i] in is_flag and list1[i+1] in is_num:
                flag=list1[i]
            elif list1[i] not in is_num and len(list2)>0:
                break            
            else:
                list2.append(ascii2integer[list1[i]])      
        
        ret=0      
        for j in list2:
            ret=ret*10+j
       
        if flag=='-':
            ret=ret*-1
            
        if ret>=-2147483648 and ret<=2147483647: 
            return ret
        elif ret<-2147483648:
            return -2147483648
        elif ret>2147483647: 
            return 2147483647
        
