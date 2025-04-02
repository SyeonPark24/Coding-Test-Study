import math

def solution(progresses, speeds):
    answer = []
    temp = 0  # 현재 배포 그룹의 기준일
    for i in range(len(progresses)):
        # 해당 기능이 완료되는 날짜 계산 (올림)
        days_needed = math.ceil((100 - progresses[i]) / speeds[i])

        # 현재 배포 그룹보다 오래 걸리면 → 새 그룹 시작
        if days_needed > temp:
            temp = days_needed
            answer.append(1)  # 새로운 그룹에 첫 기능 추가
        else:
            answer[-1] += 1  # 현재 그룹에 기능 추가

    return answer