from collections import deque
from typing import List, Deque

# this one is O(n log n). It uses a binary search to make optimal inserts. Insert with a List is O(N) at worst.
class Solution:

    def sortedSquares(self, nums: List[int]) -> List[int]:
        if not self.fully_sorted(nums) :
            self.sort_as_absolute_numbers_bigoh_nsquared(nums)

        self.square(nums)
        return nums

    def sortedSquares2(self, nums: List[int]) -> List[int]:
        if not self.fully_sorted(nums) :
            self.sort_as_absolutes_bigoh_n(nums)

        self.square(nums)
        return nums

    def sort_as_absolutes_bigoh_n(self, nums: List[int])-> None:
        nums_deque: Deque[int] = deque(nums)

        self.sort_as_absolutes_with_deque(nums_deque)

        nums.clear()
        nums.extend(nums_deque)

    def sort_as_absolutes_with_deque(self, nums: Deque[int]) -> None:
        positive_index: int = len(nums) - 1

        while nums[0] < 0 :
            if abs(nums[0]) >= nums[positive_index] :
                nums.insert(positive_index + 1, abs(nums[0]))
                nums.popleft()
            else : positive_index -= 1

    def sort_as_absolute_numbers_bigoh_nsquared(self, nums: List[int]) -> None:
        positive_start_index: int = self.find_positive_position(nums)
        insert_left_of_here: int = -1

        while positive_start_index > 0 :
            absolute_value = abs(nums[0])
            nums.pop(0)
            positive_start_index -= 1
            insert_left_of_here = self.discover_earliest_index_of_larger_number(absolute_value, nums, positive_start_index, len(nums) - 1)
            nums.insert(insert_left_of_here, absolute_value)

    @staticmethod
    def fully_sorted(nums: List[int]) -> bool:
        if nums[0] > -1 : return True
        else: return False

    @staticmethod
    def find_positive_position(nums: List[int]) -> int:
        if len(nums) == 1 : return 0

        for i in range(len(nums)) :
            if nums[i] > -1 : return i

        return len(nums)

    @staticmethod
    def discover_earliest_index_of_larger_number(number_to_insert: int, nums: List[int], left_most_index: int, right_most_index: int) -> int:
        while left_most_index < right_most_index :
            offset_to_mid: int = (right_most_index - left_most_index) // 2
            mid_index = left_most_index + offset_to_mid
            if number_to_insert == nums[mid_index] :
                return mid_index
            elif number_to_insert < nums[mid_index] : right_most_index = mid_index - 1
            else : left_most_index = mid_index + 1

        if number_to_insert < nums[right_most_index] : return right_most_index
        else : return right_most_index + 1

    @staticmethod
    def square(nums: List[int]) -> None:
        for i in range(len(nums)) :
            nums[i] = nums[i] ** 2



if __name__ == "__main__":
    # Create a list of sorted integers from -5 to 5
    numbers = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    #numberss = [-20, -5, 4, 9, 10]
    #numberss = [-2]
    original_nums = numbers.copy()

    # Create an instance of the Solution class
    solution = Solution()

    # Call the sortedSquares method and store the result
    result = solution.sortedSquares2(numbers)

    # Print the final result
    print("Original sorted list of integers:", original_nums)
    print("List of squared elements in sorted order:", result)