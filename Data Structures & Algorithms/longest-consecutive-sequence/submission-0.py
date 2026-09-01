class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sortednums = sorted(set(nums))

        longest = 1
        count = 1

        for i in range(1, len(sortednums)):
            if sortednums[i] == sortednums[i - 1] + 1:
                count += 1
            else:
                longest = max(longest, count)
                count = 1

        return max(longest, count)