from collections import deque
from typing import List
from typing import Deque

# Interesting that this solution is in the bottom 5% for execution but top 95% for memory.
# When I refactored the code to not use any class instance variables or methods, it got higher in 6.9% for
# execution and became mediocre for memory. I wonder if the other python solutions used bit manipulation which would be a good fit for this problem.

class Solution:
    def __init__(self):
        self.flipped_locations : Deque[int] = deque()
        self.left_index = self.right_index = self.max_number_of_ones = 0

    def longestOnes(self, nums: List[int], k: int) -> int:

        while self.right_index < len(nums):
            if nums[self.right_index] == 1:
                self.max_number_of_ones = max(self.max_number_of_ones, self.right_index - self.left_index + 1)
                self.right_index += 1
            elif nums[self.right_index] == 0:
                if len(self.flipped_locations) < k :
                    self.flip(self.right_index, nums)
                    self.max_number_of_ones = max(self.max_number_of_ones, self.right_index - self.left_index + 1)
                    self.right_index += 1
                else:
                    if len(self.flipped_locations) > 0:
                        self.left_index = self.flipped_locations.popleft() + 1
                    else :
                        self.right_index += 1
                        self.left_index = self.right_index

        return self.max_number_of_ones

    def flip(self, index: int, nums: List[int]) -> None:
        nums[index] = 1
        self.flipped_locations.append(index)
