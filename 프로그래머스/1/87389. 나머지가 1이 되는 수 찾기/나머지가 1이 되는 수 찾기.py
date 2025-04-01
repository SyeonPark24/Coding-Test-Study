def solution(n):
    list_a = []
    
    
    for i in range(1, n):
        if n%i ==1:
            list_a.append(i)
            
    if list_a and min(list_a) <=n-1:
        answer = min(list_a)
        
    else : 
        answer = n-1
        
    return answer