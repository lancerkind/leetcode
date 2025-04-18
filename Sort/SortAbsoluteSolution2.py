from collections import deque
from typing import List, Deque

# This one is close to O(n) but is unfortunetaly O(n^2) due to deque.insert.
class Solution:

    def sortedSquares(self, nums: List[int]) -> List[int]:
        self.sort_as_absolutes_bigoh_n(nums)
        self.square(nums)
        return nums

    def sort_as_absolutes_bigoh_n(self, nums: List[int])-> None:
        nums_deque: Deque[int] = deque(nums)

        self.sort_as_absolutes_with_deque(nums_deque)

        nums.clear()
        nums.extend(nums_deque)

    @staticmethod
    def sort_as_absolutes_with_deque(nums: Deque[int]) -> None:
        positive_index: int = len(nums) - 1

        while nums[0] < 0 :
            if abs(nums[0]) >= nums[positive_index] :
                nums.insert(positive_index + 1, abs(nums[0]))
                nums.popleft()
            else : positive_index -= 1

    @staticmethod
    def square(nums: List[int]) -> None:
        for i in range(len(nums)) :
            nums[i] = nums[i] ** 2

if __name__ == "__main__":
    # Create a list of sorted integers from -5 to 5
    #numbers = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    #numbers = [-20, -5, 4, 9, 10]
    numbers = [-2]

    original_nums = numbers.copy()

    # Create an instance of the Solution class
    solution = Solution()

    # Call the sortedSquares method and store the result
    result = solution.sortedSquares(numbers)

    # Print the final result
    print("Original sorted list of integers:", original_nums)
    print("List of squared elements in sorted order:", result)