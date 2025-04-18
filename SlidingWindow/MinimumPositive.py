from typing import List

class Solution:

    def minStartValue(self, nums: List[int]) -> int:
        summation = self.prefix_sum(nums)
        min_num = 1

        for number in summation:
            min_num = min(min_num, number)

        return min_num if min_num > 0 else abs(min_num) + 1 # if min_num is < 0, then need to add +1 to become a positive number.

    @staticmethod
    def prefix_sum(nums: List[int]) -> List[int]:
        result: List[int] =[0]

        for number in nums:
            result.append(result[-1] + number)

        return result[1:]


