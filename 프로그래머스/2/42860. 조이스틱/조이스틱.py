def solution(name):
    # 알파벳 변경 횟수
    spell_move = 0
    
    # 커서 이동 횟수 (좌우 이동 끝까지 가는 경우)
    cursor_move = len(name) - 1
    
    for i, spell in enumerate(name):
        # 알파벳 변경 횟수, 위 아래 중 최소 이동 값
        ## 위로 몇번 이동해야하는지, 아래로 몇번 이동해야하는지 
        spell_move += min(ord(spell) - ord('A'), ord('Z') - ord(spell) + 1)
        
        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
            
        # 왼쪽으로 돌고 오는 방법  vs 오른쪽으로 끝까지 가는 방법 중 가장 짧은거리    
        cursor_move = min([cursor_move, 
                           2*i + len(name)-next,
                          i + 2*(len(name)-next)])
        
    return spell_move + cursor_move


