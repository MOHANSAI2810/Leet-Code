class Solution:
    def judgeCircle(self, moves: str) -> bool:
        a=0
        b=0
        for i in moves:
            if i =='R':
                a+=1
            elif i=="L":
                a-=1
            elif i=="U":
                b+=1
            elif i=="D":
                b-=1
        if a==0 and b==0:
            return True
        else:
            return False
