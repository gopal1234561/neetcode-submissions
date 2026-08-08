class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans=list(digits)
        for i in range(len(ans)-1, -1, -1):
            if ans[i] < 9:
                ans[i] += 1
                return ans
            ans[i] = 0
            
        return [1] + ans