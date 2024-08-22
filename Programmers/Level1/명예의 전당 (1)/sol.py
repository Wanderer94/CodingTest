def solution(k, score):
    answer = []
    HOF = []
    for i in score:
        if HOF == []:
            HOF.append(i)
        elif len(HOF) < k:
            HOF.append(i)
            HOF.sort(reverse = True)
        elif HOF[-1] < i and len(HOF) == k:
            HOF.pop()
            HOF.append(i)
            HOF.sort(reverse = True)
        answer.append(HOF[-1])
    return answer