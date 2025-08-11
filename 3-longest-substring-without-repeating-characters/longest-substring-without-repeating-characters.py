class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        max_len = 0
        left, right = 0,0

        while right<len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            max_len = max(max_len,right-left+1)
            right += 1
        
        return max_len
        
        