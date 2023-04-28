class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j=0
        c=len(nums)
        while(val in nums):
            nums.remove(val)
        print nums
