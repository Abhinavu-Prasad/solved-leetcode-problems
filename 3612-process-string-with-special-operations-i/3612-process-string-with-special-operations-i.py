class Solution:
    def processStr(self, s: str) -> str:
        l = []
        for i in s:
            if i == "*" :
                if l != []:
                    l.pop()
                else:
                    continue
            elif i == "#":
                l.extend(l)
            elif i == "%":
                l = l[::-1]
            else:
                l.append(i)
        return "".join(l)