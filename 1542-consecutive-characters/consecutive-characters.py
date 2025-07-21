from collections import Counter
class Solution(object):
    def maxPower(self, s):
        power = 0
        for i in range(len(s)):
            count = 0
            for j in range(i,len(s)):
                if s[i] == s[j]:
                    count += 1
                else:
                    break
            if count>power:
                power = count
        return power
