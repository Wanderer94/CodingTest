def solution(N, stages):
    answer = [0] * N
    # 성공 여부 확인
    for i in stages:
        if i <= N:
            for j in range(i-1):
                answer[j] += 1
        else:
            for j in range(N):
                answer[j] += 1
    #실패율 계산
    n = len(stages)
    rate = []
    for i in answer:
        rate.append((n-i)/n)
        n = i
    sort_rate = sorted(rate, reverse = True)
    
    #답안 확인
    ans = []
    for i in sort_rate:
        ans.append(rate.index(i)+1)
    #같은 경우의 수 어떻게 해결할건지 문제
    return ans