from typing import List
class Solution:
    def check(self, nums: List[int]) -> bool:
        # 3 < 4
        # 4 < 5
        # 5 < 1 drop
        # 1 < 2
        # check 3 < 2 False
        # 2 < 1 drop
        # 1 < 3
        # 3 < 4
        # check 2 < 4 True drop
        # 1 < 2
        # 2 < 3
        # check 1 < 3 True drop

        # base case all are sort
        drop = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                drop += 1
        # check potentail to rotate
        if nums[0] < nums[len(nums)-1]:
            drop += 1
        return drop <= 1
    
# Time complexity: O(n)
# Space complexity: O(1)

# test cases
# [3,4,5,1,2] => True
# [2,1,3,4] => False
# [1,2,3] => True

test_cases = [[3,4,5,1,2], [2,1,3,4], [1,2,3]]
print(Solution().check(test_cases[0]))
print(Solution().check(test_cases[1]))
print(Solution().check(test_cases[2]))

