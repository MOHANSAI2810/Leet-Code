class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        a=[]
        b=[]
        for i in jewels:
            a.append(i)
        for i in stones:
            b.append(i)
        c=0
        for i in b:
            if i in a:
                c+=1
        return c 
