class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=sorted(set(nums),key = nums.index)
        j = 0
        for i in s:
            nums[j] = i
            j+=1
        return len(s)



         
