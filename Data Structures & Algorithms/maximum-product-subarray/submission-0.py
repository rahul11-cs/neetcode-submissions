class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix=1
        suffix=1
        max_pro=nums[0]
        for i in range(len(nums)):
            prefix*= nums[i]
            suffix*= nums[len(nums)-1-i]

            max_pro=max( prefix, suffix, max_pro)
        return max_pro    