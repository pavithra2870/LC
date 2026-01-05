Return the minimum number of boxes you need to select to redistribute these n packs of apples into boxes.

- to use minimum boxes to pack all the apples, sort the capacity array in desc order so we use the boxes with highest capacities first itself

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
