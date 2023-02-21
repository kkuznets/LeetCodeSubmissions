import numpy as np

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct = np.prod(nums)
        products = []
        for index, value in enumerate(nums):
            if value != 0:
                productExcept = round(totalProduct / value)
            else:
                productExcept = np.prod(nums[:index] + nums[index+1:])
            products.append(productExcept)
        return products
