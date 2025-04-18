import pytest
from .Longest_Ones_Solution import Solution

@pytest.fixture
def solution(): return Solution()

def test_one_element_no_flips(solution):
    assert solution.longestOnes([1], 0) == 1

def test_one_element_no_flips_zero_case(solution):
    assert solution.longestOnes([0], 0) == 0

def test_one_element_flip(solution):
    assert solution.longestOnes([0], 1) == 1

def test_two_element_no_flip(solution):
    assert solution.longestOnes([1,1], 0) == 2

def test_two_element_oneflip(solution):
    assert solution.longestOnes([1,0], 1) == 2

def test_two_element_oneflip2(solution):
    assert solution.longestOnes([0,0], 1) == 1

def test_two_element_twoflip(solution):
    assert solution.longestOnes([0,0], 2) == 2

def test_many_element_threeflip(solution):
    assert solution.longestOnes([1,0,0,1,1,0,0,1,0,0], 3) == 6

def test_leetcode_case_1(solution):
    assert solution.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6

def test_leetcode_case_2(solution):
    assert solution.longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3) == 10

def test_four_element_no_flip(solution):
    assert solution.longestOnes([1, 0, 1], 0) == 1

def test_four_element_no_flip(solution):
    assert solution.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1], 0) == 4