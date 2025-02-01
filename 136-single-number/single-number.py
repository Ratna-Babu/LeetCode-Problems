class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique = 0
        for num in nums:
            unique ^= num
        return unique