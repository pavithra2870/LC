# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
when you list divisors, they always come in pairs:

if `i` divides `n`, then `n / i` also divides `n`

most numbers quickly end up with more than 4 divisors.
so we can stop as soon as we find too many.
# Approach
<!-- Describe your approach to solving the problem. -->
for each number in the array:

- start with a set containing `{1, n}`
- try all numbers `i` from `2` to `sqrt(n)`
- if `i` divides `n`:
  - add `i` and `n // i` to the set
- if the set size goes above 4:
  - stop early (not valid)
- at the end:
  - if the set size is exactly 4, add their sum to the answer

# Key points

- divisors come in pairs so we count fast
- checking only up to `sqrt(n)` avoids extra work
- early stopping keeps it efficient

# Complexity
- time: `o(n sqrt(m))`
- space: `o(1)` per number
# Code
```python3 []
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def is4(num):
            f=set([1,num])
            for i in range(2,int(num**0.5)+1):
                if num%i==0: 
                    f.add(i)
                    f.add(num//i)
            return sum(f) if len(f)==4 else 0
        res=0
        for num in nums:
            res+=is4(num)
        return res
```
