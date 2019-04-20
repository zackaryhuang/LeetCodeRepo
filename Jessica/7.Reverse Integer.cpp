class Solution {
public:
    int reverse(int x) {          
        int ret=0;
        while(x){
            int temp=x%10;
            if(ret>INT_MAX/10 || ret<INT_MIN/10)
                return 0;
            ret=ret*10+temp;
            x=x/10;            
        }
        return ret;
    }
    
};