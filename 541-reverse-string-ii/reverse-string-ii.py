class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)  # convert string to list for in-place modification
        
        for i in range(0, len(s), 2 * k):
            # reverse the first k characters in every 2k block
            s[i:i+k] = reversed(s[i:i+k])
        
        return ''.join(s)

        