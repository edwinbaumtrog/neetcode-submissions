class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            match c:
                case '(':
                    stack.append(c)
                case ')':
                    if not stack:
                        return False
                    if stack and stack.pop() != '(':
                        return False
                case '{':
                    stack.append(c)
                case '}':
                    if not stack:
                        return False
                    if stack and stack.pop() != '{':
                        return False
                case '[':
                    stack.append(c)
                case ']':
                    if not stack:
                        return False
                    if stack.pop() != '[':
                        return False
        if stack:
            return False
        return True