# 괄호 문자열 >> u,v로 나누는 함수
def split_uv(p):
    u = ''
    v = ''
        
    for i in range(2, len(p)+1, 2):
        if balance_check(p[:i]):
            return p[:i], p[i:] # u, v(u는 더 이상 분리 불가능이랬으니까 길이가 2일 것)

# 균형 잡힌 문자열인가?
def balance_check(s):
    left = 0
    right = 0
    for i in s:
        if i == "(":
            left+=1
        else:
            right+=1
            
    return left ==right
            

# 올바른 괄호 문자열인가?
def correct_check(s):
    stack = []
    for i in s:
        
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            else:
                stack.pop()
            
    return not stack



def solution(p):
    if p =='': # 1단계 : 더이상 쪼갤게 없다면 or 입력이 빈 문자열이라면 -> 그냥 빈문자열 반환
        return ''
    
    u, v = split_uv(p) # 2단계 : 먼저 u,v로 분리 
        
    if correct_check(u) : # u가 올바르다면 
        return u + solution(v)
            
    else :  # u가 올바르지 않다면
        temp = "("
        temp += solution(v)
        temp += ')'
        u = u[1:-1] # u 앞 뒤 제거
        new_u = ''
        for ch in u:
            if ch == ')':
                new_u += "("
            else:
                new_u += ")"
        temp += new_u
        return temp
