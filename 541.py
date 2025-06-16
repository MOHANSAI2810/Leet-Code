class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        print(s, k)
        a = []
        for i in s:
            a.append(i)
        print('a is', a)
        
        i = 0
        while i < len(a):
            b = []
            # Collect k characters or whatever is left
            for j in range(k):
                if i + j < len(a):
                    b.append(a[i + j])
            print('b is', b)
            c = b[::-1]
            print('c is', c)

            # Replace the portion in 'a' with reversed characters
            for j in range(len(c)):
                a[i + j] = c[j]

            i += 2 * k  # Move to the next 2k block
            print('a after update:', a)

        d = a
        e = ''.join(d)
        return e
