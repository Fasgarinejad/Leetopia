class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = [1]
        suffix = [1]
        reversed_num = nums[::-1]
        for i in range(1, len(nums)):
            prefix.append(prefix[i-1]*nums[i-1])
        for i in range(1, len(reversed_num)):
            suffix.append(suffix[i-1]*reversed_num[i-1])
        #print(prefix, suffix[::-1])
        return [m*n for m,n in zip(prefix, suffix[::-1])]

# nums = [1, 2, 3, 4]
nums = [-1, 1, 0, -3, 3]
sol = Solution()
sol.productExceptSelf(nums)


