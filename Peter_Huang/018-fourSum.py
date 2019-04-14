class Solution(object):
    def threeSum(self, q,b):
        """
        :type q: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(len(q)):
            if i == 0 or q[i] > q[i-1]:
                left = i+1
                right = len(q)-1
                while left < right:
                    sum = q[i] + q[left] + q[right]
                    if sum == b:
                        temp = [q[i],q[left],q[right]]
                        res.append(temp)
                        left += 1
                        right -= 1
                        while left < right and q[left] == q[left-1]:
                            left += 1
                        while left < right and q[right] == q[right+1]:
                            right -= 1
                    elif sum > b:
                        right -= 1
                    else:
                        left += 1
        return res
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        a = []
        c = []
        while len(nums) >= 4:
            print(nums[0])
            if nums[0] in a:
                nums = nums[1:]
                continue
            else:
                d = self.threeSum(nums[1:],target-nums[0])
                if d == []:
                    nums = nums[1:]
                    continue
                else:
                    for item in d:
                        item.insert(0,nums[0])
                    print('d_____',d)
                    a.append(nums[0])
                    c += d
                    nums = nums[1:]
        return c

if __name__ == "__main__":
    s = Solution()
    res = s.fourSum([1,2,3,4,6,9],15)
    print('res____',res)
    