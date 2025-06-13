class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = []
        for i in s:
            if i.isalnum():  # only consider alphanumeric characters
                a.append(i.lower())  # convert to lowercase
        if a==a[::-1]:
            return True
        else:
            return False  
