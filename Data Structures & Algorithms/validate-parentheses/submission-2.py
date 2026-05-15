class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        res = {"}": "{", ")": "(", "]": "["}
        for each in s:
            if each == "[" or each == "(" or each == "{":
                stack.append(each)
            elif stack and res.get(each) == stack[-1]:
                stack.pop()
            else:
                return False
        print(stack)
        return True if not len(stack) else False
