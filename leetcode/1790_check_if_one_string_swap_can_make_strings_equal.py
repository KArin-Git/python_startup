class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # base case first == last
        if s1 == s2:
            return True
        # finding mismatch
        # b == k False
        # k == b False
        # swab
        # check after swap is matched or not
        first, last = 0, len(s2) - 1
        while s1[first] == s2[first]:
            first += 1
        while s1[last] == s2[last]:
            last -= 1
        s2 = list(s2)
        s2[first], s2[last] = s2[last], s2[first]
        s2 = ''.join(s2)
        return s1 == s2
    
# Time complexity: O(n)
# Space complexity: O(n)

# test cases
# s1 = "bank", s2 = "kanb" => True
# s1 = "attack", s2 = "defend" => False
# s1 = "kelb", s2 = "kelb" => True
# s1 = "abcd", s2 = "dcba" => False
test_cases = [["bank", "kanb"], ["attack", "defend"], ["kelb", "kelb"], ["abcd", "dcba"]]
print(Solution().areAlmostEqual(test_cases[0][0], test_cases[0][1]))
print(Solution().areAlmostEqual(test_cases[1][0], test_cases[1][1]))
print(Solution().areAlmostEqual(test_cases[2][0], test_cases[2][1]))
print(Solution().areAlmostEqual(test_cases[3][0], test_cases[3][1]))