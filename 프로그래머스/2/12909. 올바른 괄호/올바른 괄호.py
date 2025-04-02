def solution(s):

    stack = []
    
    for i in s :
        if i == '(':
            stack.append('(')
        
        else : # i == ')' 인 경우
            if not stack:
                return False
            
            else:
                stack.pop()
    
    if stack :
        return False
    
    return True