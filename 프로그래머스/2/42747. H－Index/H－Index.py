def solution(citations):
    
    h_list = []
    
    for i in range(max(citations)+1):
        cnt = 0 
        for j in citations:
            if j >= i:
                cnt+=1
        if cnt >= i:
            h_list.append(i)
        
    return max(h_list) if h_list else 0