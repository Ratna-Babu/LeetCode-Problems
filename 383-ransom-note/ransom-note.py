class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        
        freq = {}
        
        for ch in magazine:
            freq[ch] = freq.get(ch,0) + 1
        
        for ch in ransomNote:
            if ch in freq:
                if freq[ch] == 0:
                    return False
                elif freq[ch] > 0:
                    freq[ch] -= 1
            else:
                return False
        return True