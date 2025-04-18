import pytest
from .Minimum_Positive import Solution

@pytest.fixture
def solution(): return Solution()

def test_one_element(solution):
    nums = [1]
    assert solution.minStartValue(nums) == 1

def test_two_element(solution):
    nums = [1, 2]
    assert solution.minStartValue(nums) == 1

def test_two_element_negative(solution):
    nums = [1, -2]
    assert solution.minStartValue(nums) == 2

def test_three_element(solution):
    nums = [-5, 2, -2]
    # -5, -3, -5
    assert solution.minStartValue(nums) == 6

def test_four_element(solution):
    nums = [8, -10, -25, 50]
    assert solution.minStartValue(nums) == 28