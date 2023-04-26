# def solution(answers):
#     answer = []
#     ans1 = [1,2,3,4,5]
#     ans1_c = 0
#     ans2 = [2,1,2,3,2,4,2,5]
#     ans2_c = 0
#     ans3 = [3,3,1,1,2,2,4,4,5,5]
#     ans3_c = 0
#     for i in range(len(answers)):
#         if answers[i] == ans1[i%5]:
#             ans1_c += 1
#         elif answers[i] == ans2[i%8]:
#             ans2_c += 1
#         elif answers[i] == ans3[i%10]:
#             ans3_c += 1
#     max_c = max(ans1_c,ans2_c,ans3_c)
#     if max_c == ans1_c:
#         answer.append(1)
#     elif max_c == ans2_c:
#         answer.append(2)
#     elif max_c == ans3_c:
#         answer.append(3)
#     return answer
# elif는 연속된다 if문에 연관되는지 아닌지 독립성에 대해서 생각해보기
def solution(answers):
    answer = []
    ans1 = [1,2,3,4,5]
    ans1_c = 0
    ans2 = [2,1,2,3,2,4,2,5]
    ans2_c = 0
    ans3 = [3,3,1,1,2,2,4,4,5,5]
    ans3_c = 0
    for i in range(len(answers)):
        if answers[i] == ans1[i%5]:
            ans1_c += 1
        if answers[i] == ans2[i%8]:
            ans2_c += 1
        if answers[i] == ans3[i%10]:
            ans3_c += 1
    max_c = max(ans1_c, ans2_c, ans3_c)
    if max_c == ans1_c:
        answer.append(1)
    if max_c == ans2_c:
        answer.append(2)
    if max_c == ans3_c:
        answer.append(3)
    
    return answer