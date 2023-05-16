class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s=""
        for i in digits:
            s+=str(i)
        x=int(s)
        x=x+1
        x=str(x)
        l=[]
        for i in x:
            l.append(i)
        res = [int(i) for i in l]
        return(res)
