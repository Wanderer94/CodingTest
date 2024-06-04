def solution(id_list, report, k):
    #신고내역 정리
    answer = [[] for _ in range(len(id_list))]
    for i in report:
        a = i.split()
        b = id_list.index(a[1])
        answer[b].append(a[0])
    #정지 여부 확인
    result = [ False for _ in range(len(id_list))]
    for i in answer:
        j = list(set(i))
        if len(j) == k:
            result[answer.index(i)] = True
    #메일 발송 과정
    ans = [0 for _ in range(len(id_list))]
    for i in range(len(result)):
        if result[i] == True:
            for j in answer[i]:
                ans[id_list.index(j)] += 1  
    return ans