from collections import defaultdict
from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        freq = defaultdict(int)

        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                freq[product] += 1
        
        res = 0

        for f in freq.values():
            if f > 1:
                res += (f * (f - 1) // 2) * 8

        return res
    
# Example test case
nums = [2, 3, 4, 6]
solution = Solution()
print(solution.tupleSameProduct(nums))  # Output: 8