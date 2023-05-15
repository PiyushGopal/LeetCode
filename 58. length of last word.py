class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        flag = 2
        sum = 0
        if len(s) == 1:
            if len(s)== " ":
                return 0
            else:
                return 1
        for i in range(len(s)-1,-1,-1):
            if(s[i]!=" "):
                flag = 1
                sum += 1
            elif(s[i]==" " and flag ==2):
                pass
            else:
                break
        return sum
