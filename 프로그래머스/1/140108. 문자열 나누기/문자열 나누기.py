def solution(s):
    
    answer = 0
    x_cnt, not_x_cnt = 0, 0
    
    for i in range(len(s)):
        
        if x_cnt == not_x_cnt: 
            answer +=1
            x = s[i]
            x_cnt, not_x_cnt = 0, 0
        
        if s[i] ==x:
            x_cnt +=1

        else:
            not_x_cnt +=1
        
    return answer