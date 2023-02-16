class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked_nums = {}
        for index, num in enumerate(nums):
            diff = target - num 
            if diff in checked_nums:
                return [nums.index(diff), index]
            checked_nums[num] = index