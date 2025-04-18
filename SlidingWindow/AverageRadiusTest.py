import pytest
from SlidingWindow.AverageRadius import Solution

@pytest.fixture
def solution(): return Solution()

def test_running_sum(solution):
    assert solution.running_sum([1, 6]) == [0, 1, 7]

def test_running_sum_empty(solution):
    assert solution.running_sum([]) == [0]

def test_running_sum_single(solution):
    assert solution.running_sum([7]) == [0, 7]

def test_window_too_large(solution):
    assert solution.getAverages([1, 2, 3, 4, 5], 6) == [-1, -1, -1, -1, -1]

def test_average_radius_single(solution):
    assert solution.getAverages([5], 0) == [5]

def test_average_radius_double(solution):
    assert solution.getAverages([5, -1], 0) == [5, -1]

def test_average_radius_radius_1(solution):
    assert solution.getAverages([1, 2, 3], 1) == [-1, 2, -1]
    # [1, 3, 6] average == 6 - 1 // 3 == 5//3 == 1

def test_average_radius_quattro_radius_1(solution):
    assert solution.getAverages([1, 2, 3, -8], 1) == [-1, 2, -1, -1]
    # [1, 3, 6] average == 6 - 1 // 3 == 5//3 == 1
def test_average_radius_radius_3_too_big(solution):
    assert solution.getAverages([1, 2, 3, 4, 5, 6], 3) == [-1, -1, -1, -1, -1, -1]

def test_average_radius_radius_3(solution):
    assert solution.getAverages([1, 1, 1, 1, 1, 1, 1], 3) == [-1, -1, -1, 1, -1, -1, -1]

def test_average_radius_radius_3_zero(solution):
    assert solution.getAverages([1, 1, 1, -4, 1, 1, 1], 3) == [-1, -1, -1, 0, -1, -1, -1]
