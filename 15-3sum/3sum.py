class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)

        result = []

        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue  
            j = i+1
            k = len(nums)-1

            while j<k:
                total_sum = nums[i]+nums[j]+nums[k]
                if total_sum == 0:
                    result.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif total_sum > 0:
                    k -= 1
                else:
                    j += 1

        return result
