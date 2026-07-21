class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {")": "(", "]":"[", "}":"{"}

        for x in s:
            if x in dictionary:
                if stack and (stack[-1]==dictionary[x]):
                    stack.pop()

                else:
                    return False

            else:
                stack.append(x)
        
        if not stack:
            return True

        else:
            return False