# Time complexity: O(n)
# Space complexity: O(n)
def isValid(s: str) -> bool:
    stack = []
    if(len(s) % 2 == 0):
        for elem in s:
            if (elem == "(" or
                elem == "{" or
                elem == "["):
                stack.append(elem)
            elif(len(stack) != 0):
                if((elem == ")" and stack[-1] == "(") or
                    (elem == "}" and stack[-1] == "{") or
                    (elem == "]" and stack[-1] == "[")):
                    stack.pop()
                else:
                    return False
            else:
                return False
    else:
        return False
    
    if len(stack) == 0:
        return True
    else:
        return False



# Test 
print(isValid("()"))       