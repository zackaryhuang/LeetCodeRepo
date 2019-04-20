class Solution {
public:
    bool isPalindrome(int x) {
          if (x<0)
            return false;
        else if(x<10 && x>=0)
            return true;
        else{
            int reverse = 0;
            int y=x;
            while(y>0){
                reverse=(reverse*10)+(y%10);
                
                y=y/10;
            }
            if(reverse == x)
                return true;
            else
                return false;
                  
                
            
             
        }
    }
};