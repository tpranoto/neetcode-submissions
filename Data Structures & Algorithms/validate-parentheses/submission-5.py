class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == ")" and len(stack)>0 and stack[-1] == "(":
                stack.pop()
                continue
            if c == "]" and len(stack)>0 and stack[-1] == "[":
                stack.pop()
                continue
            if c == "}" and len(stack)>0 and stack[-1] == "{":
                stack.pop()
                continue
            stack.append(c)

        return len(stack) == 0
