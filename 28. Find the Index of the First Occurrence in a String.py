class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        j=0
        i = 0
        result = []
        if needle in haystack:
            while(i<len(haystack)):
                if haystack[i]==needle[j]:
                    result.append(i) 
                    j+= 1
                else:
                    i -= len(result)
                    result = []
                    j = 0
                if len(result) == len(needle):
                    return result[0]
                i += 1
        else:
            return -1
