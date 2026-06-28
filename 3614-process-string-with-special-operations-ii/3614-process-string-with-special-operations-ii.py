class Solution:
    def processStr(self, s: str, k: int) -> str:
        lengths = []
        curr = 0

        for ch in s:
            if 'a' <= ch <= 'z':
                curr += 1
            elif ch == '*':
                if curr > 0:
                    curr -= 1
            elif ch == '#':
                curr *= 2
            else:  # %
                pass

            lengths.append(curr)

        if k >= curr:
            return '.'

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            curr = lengths[i]

            if 'a' <= ch <= 'z':
                if k == curr - 1:
                    return ch

            elif ch == '*':
                pass

            elif ch == '#':
                half = curr // 2
                k %= half

            else:  # %
                k = curr - 1 - k

        return '.'