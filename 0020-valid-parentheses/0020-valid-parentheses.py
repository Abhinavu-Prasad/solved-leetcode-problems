class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == "{" or i == "[" or stack == []:
                stack.append(i)
            elif i == ")" and stack != []:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif i == "}" and stack != []:
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            elif i == "]" and stack != []:
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True
            
            
            