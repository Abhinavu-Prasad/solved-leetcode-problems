class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        result = []
        for i in range(12):
            for j in range(60):
                if bin(i).count("1") + bin(j).count("1") == turnedOn:
                    if j >= 10:
                        result.append(f"{i}:{j}")
                    else:
                        result.append(f"{i}:0{j}")
        return result