## LC 67: Add Binary Strings
```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m,n=len(a),len(b)
        maxx=max(m,n)
        a,b=a[::-1],b[::-1]
        res=""
        c=0
        for i in range(maxx):
            e,f=ord(a[i])-ord('0') if i<m else 0, ord(b[i])-ord('0') if i<n else 0
            # -ord('0') because ord('0')=48 not 0. so gotta subtract
            g=e+f+c
            res=str(g%2)+res
            c=g//2
        return res if c==0 else "1"+res
```

## LC 190: Reverse Bits
```python
class Solution:
    def reverseBits(self, n: int) -> int:
        res=0
        for _ in range(32):
            res = (res<<1)|(n&1)
            n>>=1
        return res
```

## LC 401: Binary Watch
```python
class Solution:
    def readBinaryWatch(self, on: int) -> List[str]:
        h=defaultdict(list)
        m=defaultdict(list)
        h[0]=["0"]
        m[0]=["00"]
        for i in range(1,60):
            no=bin(i)[2:].count("1")
            if i<10:
                h[no].append(str(i))
                m[no].append("0"+str(i))
            else:
                if i<12: h[no].append(str(i))
                m[no].append(str(i))
        res=[]
        for i in range(on+1):
            r=on-i
            if i in h and r in m:
                for a in h[i]:
                    for b in m[r]:
                        res.append(a+":"+b)
        return res
```
## LC 693: Alternating Bits
```python
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        m=len(bin(n)[2:])
        a=n^(n>>1)
        return a&(a+1)==0 

        # let n=10 = 1010
        # n>>1 = 0101 (right shift)
        # if alternating -> n^(n>>1)=1111 (all ones)
        # if all ones, a+1 wud be 10000
        # a&(a+1) shud be 0 then
```

## LC 696: Count Binary Substrings
```python
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        last=s[0]
        cur=1
        res=prev=0
        for num in s[1:]:
            if num==last: cur+=1
            else: 
                res+=min(cur,prev)
                prev=cur
                cur=1
                last=num
        res+=min(cur,prev)
        return res
```
