def isbalanced(str):
    stack=[]

    for char in (str):
        if char in ["(", "{", "["]:
            stack.append(char)
            
        elif char in [")","}","]"]:

            
            if len(stack) == 0:
                return False
            else:
                top=stack.pop()
                
                if (top == "(" and char != ")") or (top == "[" and char !="]") or (top =="{" and char !="}"):
                    return False
    if stack:
        return False
    return True

print(isbalanced("454foo([])"))