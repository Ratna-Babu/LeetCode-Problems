class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        window_size = 3
        count = 0

        for i in range(len(s)):
            window = s[i:window_size+i]
            if len(set(window))==3:
                count += 1
        
        return count