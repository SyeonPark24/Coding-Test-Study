def solution(participant, completion):
    answer_dict = {}
    
    for name in completion:
        answer_dict[name] = answer_dict.get(name, 0) + 1
        
    for name in participant:
        if name not in answer_dict or answer_dict[name]==0 :
            return name
        else :
            answer_dict[name] -= 1