class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        StepOne=1
        StepTwo=2
        ret=0
        for i in range(3,n+1):
            ret=StepOne+StepTwo
            StepOne=StepTwo
            StepTwo=ret
        return ret
            
        