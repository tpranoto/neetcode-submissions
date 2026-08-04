class Solution:
    def decodeString(self, s: str) -> str:
        result = ""
        k = 0
        count_stack = []
        string_stack = []

        for c in s:
            if c.isdigit():
                k = int(c) + (k *10)
            elif c == "[":
                string_stack.append(result)
                count_stack.append(k)
                result = ""
                k = 0
            elif c == "]":
                prev = string_stack.pop()
                count = count_stack.pop()
                result = prev + result * count
            else:
                result += c

        return result