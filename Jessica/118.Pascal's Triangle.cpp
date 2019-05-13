class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        
        vector<vector<int>> res;
        for(int i=1;i<=numRows;i++){
            if(i==1 || i==2) {vector<int> temp(i,1);res.push_back(temp);continue;}
            vector<int> temp(i,1);
            for(int j=1;j<i-1;j++){
                temp[j] = res[i-2][j-1] + res[i-2][j];    
            }
            res.push_back(temp);
        }
        return res;
    }
    
};
