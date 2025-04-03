from itertools import permutations, combinations


def solution(k, dungeons):
    
    answer = []
    
    for dun in permutations(dungeons):
        hp = k
        dun_num = 0
        
        for minimum, consume in dun:
            
            if hp >= minimum:
                hp = hp - consume
                dun_num +=1
            
            else : 
                break  
                
            answer.append(dun_num)
               
            
    return max(answer)