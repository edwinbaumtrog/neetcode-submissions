class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in '+-*/':
                val2 = stack.pop()
                val1 = stack.pop()
                tok = 0
                match token:
                    case '+':
                        tok = val1 + val2
                    case '-':
                        tok = val1 - val2
                    case '*':
                        tok = val1 * val2
                    case '/':
                        tok = val1 / val2
                stack.append(int(tok))
            else:
                stack.append(int(token))
        return stack[-1]