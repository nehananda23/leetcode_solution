class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap={}
        for i in range(len(nums)):
            deff=target-nums[i]
            if deff in hashmap:
                return (hashmap[deff],i)
            hashmap[nums[i]]=i    
        