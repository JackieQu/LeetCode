# coding: utf-8

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None: return 0
        
        maxLen = 1 
        subStr = ""
        for letter in s:
            if letter not in subStr:
                subStr += letter
            else:
                if len(subStr) > maxLen:
                    maxLen = len(subStr)
                subStr += letter
                subStr = subStr[subStr.index(letter) + 1:]
        if len(subStr) > maxLen:
            maxLen = len(subStr)
        return maxLen

def test():
    s = Solution()
    rs = s.lengthOfLongestSubstring("abcedfckklmongkf")
    print rs

test()