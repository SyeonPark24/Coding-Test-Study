def solution(food):
    
    player_1 = ''
    
    for i in range (1, len(food)):
        player_1 += str(i) * (food[i]//2)
    
    answer= player_1 + "0" + player_1[::-1]

    return answer