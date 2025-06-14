class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = []
        b = []
        for i in s:
            a.append(i)
        for i in t:
            b.append(i)

        c = sorted(a)
        d = sorted(b)

        for i in range(len(c)):
            if c[i] != d[i]:
                return d[i]  

        return d[-1]  
