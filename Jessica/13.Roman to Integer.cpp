class Solution {
public:
     int romanToInt(string s) {
          map<char, int> RomanNum = { 
               { 'I' , 1 },
               { 'V' , 5 },
               { 'X' , 10 },
               { 'L' , 50 },
               { 'C' , 100 },
               { 'D' , 500 },
               { 'M' , 1000 } };
                                   
   int sum = RomanNum[s.back()];
   for (int i = s.length() - 2; i >= 0; --i) 
   {
       if (RomanNum[s[i]] < RomanNum[s[i + 1]])
       {
           sum -= RomanNum[s[i]];
       }
       else
       {
           sum += RomanNum[s[i]];
       }
   }
   
   return sum;
       
    }
};