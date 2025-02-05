from typing import List
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # 10 < 20 then 10 + 20 
        # 20 < 30 then 10 + 20 + 30
        # 30 not < 5 then sum_asc = 10 + 20 + 30
        # 5 < 10 then 5 + 10
        # 10 < 50 then 5 + 10 + 50
        # if sum_asc < 5 + 10 + 50
        # then sum_asc = 5 + 10 + 50
        
        # base case 1 value in list
        max_sum = 0
        sum_asc = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] <= nums[i]:
                sum_asc += nums[i]
            else:
                # compare max_sum
                max_sum = max(max_sum, sum_asc)
                sum_asc = nums[i]
        return max(max_sum, sum_asc)
        
# Time complexity: O(n)
# Space complexity: O(1)

# test cases
# [10,20,30,5,10,50] => 65
# [10,20,30,40,50] => 150
# [12,17,15,13,10,11,12] => 33
# [100,10,1] => 100
# [1] => 1
# [5,5,6,6,6,9,1,2] => 37
# [5,6,6,6,9,1,2] => 32
test_cases = [[10,20,30,5,10,50], [10,20,30,40,50], [12,17,15,13,10,11,12], [100,10,1], [1], [5,5,6,6,6,9,1,2], [5,6,6,6,9,1,2]]
print(Solution().maxAscendingSum(test_cases[0]))
print(Solution().maxAscendingSum(test_cases[1]))
print(Solution().maxAscendingSum(test_cases[2]))
print(Solution().maxAscendingSum(test_cases[3]))
print(Solution().maxAscendingSum(test_cases[4]))
print(Solution().maxAscendingSum(test_cases[5]))
print(Solution().maxAscendingSum(test_cases[6]))
