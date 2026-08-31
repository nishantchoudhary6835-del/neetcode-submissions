class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count1=0
        maxcount=0
        for i in range(len(nums)):
            if nums[i]==1:
                count1+=1
                maxcount=max(maxcount,count1)
            else:
                count1=0
        return maxcount
        