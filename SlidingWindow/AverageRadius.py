from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0: return nums

        averages: list[int] = [-1] * len(nums)
        if k > (len(nums) - 1) // 2 : return averages # if window too large, return averages

        averages_index = k # already averaged the left side window edge due to initialization, so skip it.
        running_sum = self.running_sum(nums)
        averages[averages_index] = running_sum[averages_index + k + 1] // (2 * k + 1) # edge case for when window abuts front of array where there is no prefix
        averages_index += 1

        while averages_index < len(averages) - k : # already averaged the right-side window-edge due to initialization, so skip it.
            averages[averages_index] = (running_sum[averages_index + k + 1] - running_sum[averages_index - k]) // (2 * k + 1)
            averages_index += 1
        return averages

    @staticmethod
    def running_sum(nums: List[int]) -> List[int]:
        result: List[int] =[0]
        for number in nums:
            result.append(result[-1] + number)

        return result