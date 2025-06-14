class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=[]
        b=[]
        for i in s:
            a.append(i)
        for i in t:
            b.append(i)
        c=sorted(a)
        d=sorted(b)
        if c==d:
            return True
        else:
            return False
