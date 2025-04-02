def solution(nums):
    
    num_list = set(nums)
    
    if len(num_list) >= len(nums)/2:
        answer = len(nums) / 2
        
    else : 
        answer = len(num_list)
    
    return answer