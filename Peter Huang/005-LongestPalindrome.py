class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        else:
            return longest_palindromic_substring(s)
def longest_palindromic_substring(str):
    result = []
    longest_list = ''
    res = ''
    for i in range(1,(len(str))):
        res1 = ''
        res2 = ''
        temp = []
        temp.append(str[i])
        step = 1
        temp2 = []
        step2 = 1
        while(step <= i and step<=(len(str)-i-1)):
            if str[i-step] == str[i+step]:
                temp.insert(0,str[i-step])
                temp.append(str[i+step])
                step+=1
            else:
                break
        temp_str = str[:i] + ' ' + str[i:]
        temp2.append(" ")
        while(step2 <= i and step2<=(len(temp_str)-i-1)):
            if temp_str[i-step2] == temp_str[i+step2]:
                temp2.insert(0,temp_str[i-step2])
                temp2.append(temp_str[i+step2])
                step2+=1
            else:
                break
        if len(temp2) > 1:
            temp2.pop(int(len(temp2)/2))
        else:
            temp2 = []
        for item in temp2:
            res1 += item
        for item in temp:
            res2 += item
        a_b_c = ''
        if len(res1) >= len(res2):
            a_b_c = res1
        if len(res1) == 0 and len(res2) == 0:
            a_b_c = ''
        if len(res1) < len(res2):
            a_b_c = res2
        if len(a_b_c) > len(longest_list):
            longest_list = a_b_c

    return longest_list