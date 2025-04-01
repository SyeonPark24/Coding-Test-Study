def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reported = {x:0 for x in id_list} #각 유저가 신고 당한 횟수 저장할 딕셔너리
    
    # 각 피신고자(b)가 몇 번 신고당했는지 카운트
    for r in set(report):
        a, b = r.split()
        reported[b] +=1
    
    # 다시 신고 리스트를 보면서
    for r in set(report):
        a, b = r.split()
        if reported[b] >=k: # 피신고자 b가 k번 이상 신고당했으면 -> 정지된 것이므로
            answer[id_list.index(a)] +=1 # 신고자 a는 메일 받음
    


    return answer