from typing import List
from itertools import accumulate

class Solution:

    def minStartValue(self, nums: List[int]) -> int:
        min_prefix = min(accumulate(nums))

        return max(1, 1 - min_prefix)