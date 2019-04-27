class Solution {
public:
    int climbStairs(int n) { 
        if(n==1)
            return 1;
        if(n==2)
            return 2;
        int ret=0;
        int StepOne=1;
        int StepTwo=2;
        for(int i=2;i<n;i++){
            ret = StepOne+StepTwo;
            StepOne=StepTwo;
            StepTwo=ret;
                
            
        }
        return ret;
    }
};