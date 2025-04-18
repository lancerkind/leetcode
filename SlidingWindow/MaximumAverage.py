from typing import List

class MaxAverageSolution:
    def __init__(self):
        self.current_sum: float = float('-inf')
        self.WINDOW_SIZE = 0

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_average = float('-inf')
        right_index = k - 1
        left_index = 0
        self.WINDOW_SIZE = k

        if len(nums) == 1: return nums[0]
        if k > len(nums): return float('nan')

        while right_index < len(nums) :
            max_average = max(max_average, self.get_window_average(left_index, right_index, nums))
            right_index += 1
            left_index += 1

        return max_average

    def get_window_average(self, left: int, right: int, nums: List[int]) -> float:
        if left == 0 :
            self.current_sum = sum(nums[left : right + 1])
            return self.current_sum / self.WINDOW_SIZE
        else :
            self.current_sum = self.current_sum - nums[left - 1] + nums[right]
            return self.current_sum / self.WINDOW_SIZE

if __name__ == '__main__':
    #nums = [1,12,-5,-6,50,3]
    # nums = [-1]
    # nums = [.5,.5]
    nums = [8860, -853, 6534, 4477, -4589, 8646, -6155, -5577, -1656, -5779, -2619, -8604, -1358, -8009, 4983, 7063, 3104,
     -1560, 4080, 2763, 5616, -2375, 2848, 1394, -7173, -5225, -8244, -809, 8025, -4072, -4391, -9579, 1407, 6700, 2421,
     -6685, 5481, -1732, -8892, -6645, 3077, 3287, -4149, 8701, -4393, -9070, -1777, 2237, -3253, -506, -4931, -7366,
     -8132, 5406, -6300, -275, -1908, 67, 3569, 1433, -7262, -437, 8303, 4498, -379, 3054, -6285, 4203, 6908, 4433,
     3077, 2288, 9733, -8067, 3007, 9725, 9669, 1362, -2561, -4225, 5442, -9006, -429, 160, -9234, -4444, 3586, -5711,
     -9506, -79, -4418, -4348, -5891]
    k = 93
    #k = 2

    obj = Solution()
    print(obj.findMaxAverage(nums, k))
