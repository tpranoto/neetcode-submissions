class Solution:
    def isValid(self, s: str) -> bool:
        
        mapping = {
            "]":"[",
            "}":"{",
            ")":"(",
        }

        stack = []
        for c in s:
            if c=="[" or c=="{" or c=="(":
                stack.append(c)
                continue

            if stack and mapping[c] == stack[-1]:
                stack.pop()
            else:
                return False
        
        return len(stack) == 0