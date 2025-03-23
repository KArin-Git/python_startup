from typing import List
from bisect import bisect_left

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        f_negative = bisect_left(nums, 0)
        f_positive = bisect_left(nums, 1)
        negative = f_negative
        positive = len(nums) - f_positive
        return max(negative, positive)
    
from typing import List
from bisect import bisect_left

# using copilot to generate the test cases
# Assuming the Solution class is already defined as in the provided code
def test_maximum_count():
    solution = Solution()

    # Test case 1: Mixed negative, zero, and positive numbers
    nums = [-3, -2, -1, 0, 1, 2, 3]
    assert solution.maximumCount(nums) == 3, "Test case 1 failed"

    # Test case 2: Only negative numbers
    nums = [-5, -4, -3, -2, -1]
    assert solution.maximumCount(nums) == 5, "Test case 2 failed"

    # Test case 3: Only positive numbers
    nums = [1, 2, 3, 4, 5]
    assert solution.maximumCount(nums) == 5, "Test case 3 failed"

    # Test case 4: No negative or positive numbers (only zeros)
    nums = [0, 0, 0]
    assert solution.maximumCount(nums) == 0, "Test case 4 failed"

    # Test case 5: Empty list
    nums = []
    assert solution.maximumCount(nums) == 0, "Test case 5 failed"

    # Test case 6: Mixed numbers with more positives
    nums = [-2, -1, 0, 1, 2, 3, 4, 5]
    assert solution.maximumCount(nums) == 5, "Test case 6 failed"

    # Test case 7: Mixed numbers with more negatives
    nums = [-5, -4, -3, -2, -1, 0, 1]
    assert solution.maximumCount(nums) == 5, "Test case 7 failed"

    print("All test cases passed!")

# Run the test cases
test_maximum_count()