class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        for index, num in enumerate(sorted_nums[:-1]):
            if num == sorted_nums[index+1]:
                return True
        return False