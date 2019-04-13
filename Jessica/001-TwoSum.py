'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,

return [0, 1].
'''

def two_sum(num_list,target):
	index_01 = 0
	index_02 = 0
	for i in num_list:
		if target - i in num_list:
			if target - i == i:
				continue
			else:
				index_01 = num_list.index(i)
				index_02 = num_list.index(target - i)
				return [index_01,index_02]

def main():
	res = two_sum([3,3],6)
	print(res)

if __name__ == '__main__':
	main()
