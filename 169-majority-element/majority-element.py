class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter

        nums_len = len(nums)
        count = Counter(nums)
        for num in nums:
            if count[num] > (nums_len/2):
                return num