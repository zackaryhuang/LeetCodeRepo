import copy
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # total = 0
        # while(height != ([0] * len(height))):
        #     print(height)
        #     for i in range(0, len(height)):
        #         if height[i] == 0 and i > 0:
        #             if max(height[:i]) > 0 and max(height[i:]) > 0:
        #                 total += 1
        #     for j in range(0, len(height)):
        #         if height[j] > 0:
        #             height[j] -= 1
        #     while(height.count(0) > 0):
        #         height.remove(0)    
        # return total

        total = 0
        while(len(height) > 2):
            max1 = max(height)
            max1_index = height.index(max1)
            if max1 == 0:
                return total
            temp = copy.copy(height)
            temp[max1_index] = 0
            max2 = max(temp)
            max2_index = temp.index(max2)
            if max2 == 0:
                return total
            for i in range(min(max1_index, max2_index) + 1, max(max1_index, max2_index)):
                total += (min(max1, max2) - height[i])
            height = height[:min(max1_index, max2_index)] + height[max(max1_index, max2_index):]
            print(height)
        return total
if __name__ == "__main__":
    s = Solution()
    print(s.trap([0,0,0,2,0,8,6,7,7]))