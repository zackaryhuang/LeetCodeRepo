import math
class Solution:
    def myAtoi(self, str: str) -> int:
        res_list = []
        num_list_with_operations = ['-','+','0','1','2','3','4','5','6','7','8','9']
        num_list = ['0','1','2','3','4','5','6','7','8','9']
        record = str
        flag = 0
        length = len(record)
        while length != 0:
            if record[0] == ' ':
                record = record[1:] 
                flag += 1
                length -= 1
            else:
                break
        if record == '':
            return 0
        if record[0] not in num_list_with_operations:
            return 0
        if record[0] == '-':
            res_list.append('-')
            record = record[1:]
        else:
            if record[0] == '+':
                res_list.append('+')
                record = record[1:]
            else:
                if record[0] not in ['-','+']:
                    res_list.append('+')
        record_length = len(record)
        while record_length != 0:
            if record[0] in num_list:
                res_list.append(record[0])
                record = record[1:]
                record_length -= 1
            else:
                break
        num_length = len(res_list) - 1
        res = 0
        print(math.pow(2,31))
        for i in range(1,len(res_list)):
            res += int(res_list[i]) * math.pow(10,num_length-1)
            num_length -= 1
        if res_list[0] == '-':
            res = int(-res)
        else:
            res = int(res)
        if -int(math.pow(2,31)) <= res <= int(math.pow(2,31)) - 1:
            return res
        else:
            if res > math.pow(2,31) - 1:
                return int(math.pow(2,31) - 1)
            if res < -math.pow(2,31):
                return -int(math.pow(2,31))