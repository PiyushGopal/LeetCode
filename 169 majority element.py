#from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        
        
        count = Counter(nums)
        max_count = max(count.most_common(), key=lambda x: x[1])
        return(max_count[0])    
        """
        count={}

        res,maxc=0,0
        for i in nums:
            count[i]= 1 + count.get(i,0)
            res = i if count[i] > maxc else res
            maxc=max(count[i],maxc)
        return res
