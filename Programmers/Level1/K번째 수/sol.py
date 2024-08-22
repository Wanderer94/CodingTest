def solution(array, commands):
    answer = []
    for i in commands:
        if i[0] == i[1]:
            answer.append(array[i[0]-1])
            continue
        ans = array[i[0]-1:i[1]]
        ans.sort()
        print(ans)
        answer.append(ans[i[2]-1])
    return answer