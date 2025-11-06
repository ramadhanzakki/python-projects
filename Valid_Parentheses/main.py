class Solution:
    def isValid(self, s: str) -> bool:
        PARTNER_PARENTHESES = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }
        OPEN_PARENTHESES = ['(','{','[']
        stack = []

        for char in s:
            if char in OPEN_PARENTHESES:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    ch = stack.pop()
                    if PARTNER_PARENTHESES[char] != ch:
                        return False
        if stack:
            return False
        else:
            return True