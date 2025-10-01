class Solution:
    def isPalindrome(self, x: int) -> bool:
        s_x = str(x)
        reversed_s_x = s_x[::-1]
        return s_x == reversed_s_x
sol = Solution()
print(sol.isPalindrome(121))