class Solution {
public:
    string countAndSay(int n) {
       if(n==1)
            return "1";
        if(n==2)
            return "11";
        string currentStr="11";
        string ret=""; 
        for(int i=3;i<=n;i++){
           
            int count=1;
            ret="";    
            for(int j=1;j<currentStr.length();j++){
           
                if(currentStr[j] != currentStr[j-1]){
                    ret+=to_string(count)+currentStr[j-1];
                    count=1;
                }
                   
                else
                    count++;
                if(j==currentStr.length()-1)
                        ret+=to_string(count)+currentStr[j];
                else
                     continue;
                    
                
            }
            
           currentStr=ret;
            
        }
        
        return ret;
        
    }
};
