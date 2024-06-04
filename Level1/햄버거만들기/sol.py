def solution(ingredient):
    answer = 0
    ans = [1,2,3,1]
    i = 0
    while len(ingredient) - 4 != i:
        if ingredient[i:i+4] == ans:
            answer += 1
            for a in range(4):
                ingredient.pop(i)
            i = 0
            continue
        else:
            i += 1
    return answer
