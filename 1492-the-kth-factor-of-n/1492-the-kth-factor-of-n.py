class Solution:
    def factors(self,n):
        ar = []
        for i in range(1,n//2+1):
            if n%i == 0:
                ar.append(i)
        ar.append(n)
        return ar

    def kthFactor(self, n: int, k: int) -> int:
        fac = self.factors(n)
        print(fac)
        try:
            return fac[k-1]
        except Exception:
            return -1
        

    
    
