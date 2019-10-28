class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.iter(nums)
        return len(nums)
    def iter(self, nums):
        flag = nums[0]
        times = 1
        for i in range(1, len(nums)):
            if nums[i] == flag:
                times += 1
            else:
                flag = nums[i]
                times = 1
            if times > 2:
                for j in range(i, len(nums) - 1):
                    nums[j] = nums[j + 1]
                nums.pop()
                print(nums)
                if len(nums) == 2:
                    return None
                for i in range(1, len(nums)):
                    if (nums[:i]).count(nums[i]) < 3:
                        return None
                self.iter(nums)
                break


if __name__ == '__main__':
    s = Solution()
    res = s.removeDuplicates([0,0,0,0,0])
    print(res)

