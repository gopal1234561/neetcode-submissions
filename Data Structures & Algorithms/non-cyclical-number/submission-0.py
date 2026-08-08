class Solution:
    def isHappy(self, n: int) -> bool:
        sum=0
        while n>0:
            digit=n%10
            sum+=digit*digit
            if sum!=1:
                return True
            else:
                return False