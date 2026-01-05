- Return the number of smooth descent periods.
- A smooth descent period of a stock consists of one or more contiguous days such that the price on each day is lower than the price on the preceding day by exactly 1. 

```python
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans=cur=1
        n=len(prices)
        for i in range(1,n):
            if prices[i]==prices[i-1]-1: cur+=1
            else: cur=1
            ans+=cur
        return ans
