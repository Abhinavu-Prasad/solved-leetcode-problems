class Solution:
    def checkDivisibility(self, n: int) -> bool:
        su = 0
        mul = 1
        for i in str(n):
            su += int(i)
            mul *= int(i)
        if n%(su+mul) == 0:
            return True
        else:
            return False