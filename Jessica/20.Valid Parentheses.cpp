class Solution {
public:
    bool isValid(string s) {
        stack<char> S;
        for(int i=0;i<s.length();i++){
            if(s[i]=='(' || s[i]=='[' ||s[i]=='{' ){
                cout<<s[i]<<endl;
                S.push(s[i]);
            }         
            else if(!S.empty()){
                char v=S.top();
                if(s[i]==')' && v=='('){
                    S.pop();
                    continue;
                }
                   
                else if(s[i]==']' && v=='['){
                    S.pop();
                    continue;
                }
                 
                else  if(s[i]=='}' && v=='{'){
                    S.pop();
                    continue;
                }
                else
                    return false;
            }
            else
                return false;
        }
        if(S.empty())
            return true;
        else
            return false;
    }
};
