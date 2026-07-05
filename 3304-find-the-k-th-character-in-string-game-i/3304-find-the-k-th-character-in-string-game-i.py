class Solution:
    def kthCharacter(self, k: int) -> str:
        st = "a"
        while len(st) <= k :
            temp = '' + st
            for i in st:
                val = ord(i) + 1
                if val <123:
                    temp += chr(val)
                else:
                    temp += "a"
                
            st = temp
        print(st)
        return st[k-1]


