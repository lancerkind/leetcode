# perform a merge sort which will be O(n) easy peasy.
from typing import List

class Solution:

    def sortedSquares(self, nums: List[int]) -> List[int]:
        neg_and_pos = self.split_into_negatives_and_positives(nums)
        sorted_nums = self.merge_sorted_lists(neg_and_pos)
        return self.square(sorted_nums)

    @staticmethod
    def split_into_negatives_and_positives(nums: List[int]) -> (List[int], List[int]):
        negatives: List[int] = []
        positives: List[int] = []
        for num in nums:
            if num < 0:
                negatives.append(num)
            else:
                positives.append(num)
        return negatives, positives

    @staticmethod
    def merge_sorted_lists(neg_and_pos: (List[int], List[int])) -> List[int]:
        negatives, positives = neg_and_pos

        sorted_nums: List[int] = []
        negatives_index: int = len(negatives) - 1
        positives_index: int = 0
        while positives_index < len(positives) and negatives_index >= 0:
            if abs(negatives[negatives_index]) < positives[positives_index]:
                sorted_nums.append(abs(negatives[negatives_index]))
                negatives_index -= 1
            else:
                sorted_nums.append(positives[positives_index])
                positives_index += 1

        # add remainders.
        while(negatives_index >= 0):
            sorted_nums.append(abs(negatives[negatives_index]))
            negatives_index -= 1
        sorted_nums.extend(positives[positives_index:])

        return sorted_nums

    @staticmethod
    def square(nums: List[int]) -> List[int]:
        for i in range(len(nums)) :
            nums[i] = nums[i] ** 2
        return nums

if __name__ == "__main__":
    # Create a list of sorted integers from -5 to 5
    numbers = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    #numbers = [-20, -5, 4, 9, 10]
    #numbers = [-2]

    original_nums = numbers.copy()

    # Create an instance of the Solution class
    solution = Solution()

    # Call the sortedSquares method and store the result
    result = solution.sortedSquares(numbers)

    # Print the final result
    print("Original sorted list of integers:", original_nums)
    print("List of squared elements in sorted order:", result)