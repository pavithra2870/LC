### intuition

* we can flip the sign of any element any number of times
* positive values always increase the total sum
* best move is to make every value positive
* only the parity of negative numbers matters
* even negatives → all can be made positive
* odd negatives → one number must stay negative
* keep the smallest absolute value negative to minimize loss

### approach

* initialize total sum as 0
* initialize negative count as 0
* initialize minimum absolute value as infinity
* traverse the matrix
* add absolute value of each element to total
* count negative elements
* update minimum absolute value
* if negative count is odd, subtract 2 × minimum absolute value
* return total

```python
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        tot=neg=0
        minVal=float("inf")
        for row in matrix:
            for num in row:
                tot+=abs(num)
                if num<0:
                    neg+=1
                minVal=min(minVal,abs(num))
        if neg%2==0: return tot
        return tot-2*minVal
