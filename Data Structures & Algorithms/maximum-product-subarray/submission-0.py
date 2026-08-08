class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod=nums[0]
        curr=nums[0]
        for i in range(1,len(nums)):
            max_prod=max(nums[i], max_prod*nums[i])
            curr=max(curr,max_prod)
        return curr


            