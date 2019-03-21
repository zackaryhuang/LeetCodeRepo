def longest_substring(str):
    match_str = ''
    length = 0
    flag = 0
    for i in range(0,len(str)):
        for j in range(i,len(str)):
            if str[j] in match_str:
                if len(match_str) > length:
                    length = len(match_str)
                    match_str = ''
                else:
                    match_str = ''
                break
            else:
                match_str += str[j]
                if len(match_str) > length:
                    length = len(match_str)
    return length
def main():
	res = longest_substring('bbbqwert')
	print(res)
if __name__ == '__main__':
	main()