class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sumofn=(n)*(n+1)//2
        sumofnums=sum(nums)

        return sumofn-sumofnums

