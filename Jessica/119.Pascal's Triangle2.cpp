class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<vector<int>> res;
        for(int i=1;i<=rowIndex+1;i++){
            if(i==1 || i==2) {vector<int> temp(i,1);res.push_back(temp);continue;}
            vector<int> temp(i,1);
            for(int j=1;j<i-1;j++){
                temp[j] = res[i-2][j-1] + res[i-2][j];
            }
            
            res.push_back(temp);
        }
        return res[rowIndex];
        
        
    }
};

