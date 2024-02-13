# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {')': '(', ']': '[', '}': '{'}

        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
            else:
                if not stack or matches[i] != stack[-1]:
                    return False
                stack.pop()

        return len(stack) == 0
