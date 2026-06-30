class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        sum1 = 0
        sum2 = 0
        for i in costs:
            if coins >= sum2 and not(sum2+i > coins):
                sum1 += 1
                sum2 += i
            else:
                continue

        return sum1
                