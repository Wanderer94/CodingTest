def solution(food):
    answer = ''
    ans = ''
    re_ans = ''
    for i in food:
        for j in range(i//2):
            print(i//2)
            ans += str(food.index(i))
            re_ans = str(food.index(i)) + re_ans
    answer = ans + "0" + re_ans
    return answer