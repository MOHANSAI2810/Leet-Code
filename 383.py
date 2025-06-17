class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a=[]
        b=[]
        for i in ransomNote:
            a.append(i)
        for i in magazine:
            b.append(i)
        print(a,b)
        for i in a:
            if i in b:
                b.remove(i)
            else:
                return False
        return True
