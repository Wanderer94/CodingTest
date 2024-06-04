# def solution(food):
#     answer = ''
#     ans = ''
#     re_ans = ''
#     for i in food:
#         for j in range(i//2):
#             print(i//2)
#             ans += str(food.index(i))
#             re_ans = str(food.index(i)) + re_ans
#     answer = ans + "0" + re_ans
#     return answer

def solution(food):
    answer = ''
    ans = ''
    for i in range(len(food)):
        ans += str(i) * (food[i]//2)
    answer = ans + "0" + ans[::-1]
    return answer