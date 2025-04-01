def solution(array, commands):
    
    answer = []
    for value in commands:
        i,j,k = value
        slice = array[i-1 : j]
        a = sorted(slice)[k-1]
        
        answer.append(a)
    
    return answer