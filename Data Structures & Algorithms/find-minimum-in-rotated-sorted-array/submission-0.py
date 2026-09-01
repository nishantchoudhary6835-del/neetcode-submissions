class Solution:
    def findMin(self, nums: List[int]) -> int:
        numssorted=sorted(nums)
        return numssorted[0]