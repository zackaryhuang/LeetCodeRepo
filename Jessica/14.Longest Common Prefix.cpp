class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
       
        string ret="";
        int len=strs.size();
        if(len==0)
            return "";
        else if(len==1)        
            return strs[0];
        
        for(int i=0;i<strs[0].length();i++){
          
           for(int j=1;j<len;j++){
             
               if(strs[j][i] != strs[j-1][i])                   
                   return ret;                
               
               else{
                   
                   if(j==strs.size()-1)
                       ret+=strs[j][i];                     
                       
                                          
                   else
                       continue;
               }
               
               
           }
       }
           
        return ret;
    }
    
};