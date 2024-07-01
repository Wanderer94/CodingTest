def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-9):
        check = discount[i:i+10]
        join = True
        for j in range(len(want)):
            if check.count(want[j]) < number[j]:
                join = False
                break
        if join:
            answer += 1
    return answer