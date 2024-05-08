class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums, reverse=True)
        max_k = {}
        for i, num in enumerate(sorted_nums):
            if i == 0:
                max_k[num] = "Gold Medal"
            elif i == 1:
                max_k[num] = "Silver Medal"
            elif i == 2:
                max_k[num] = "Bronze Medal"
            else:
                max_k[num] = str(i + 1)
        return max_k