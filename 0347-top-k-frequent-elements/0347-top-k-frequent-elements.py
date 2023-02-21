class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}
        frequentNumbers = []
        for index, value in enumerate(nums):
            if value in numbers:
                numbers[value] += 1
            else:
                numbers[value] = 1
        for i in range(k):
            number = max(numbers, key=numbers.get)
            frequentNumbers.append(number)
            numbers.pop(number)
        return frequentNumbers

