# def solution(k, m, score):
#     answer = 0
#     arr = []
#     while len(score) != 0 :
#         arr.append(max(score))
#         score.remove(max(score))
#         if len(arr) == m:
#             answer += min(arr) * m
#             arr = []
#     return answer

# new answer

def solution(k, m, score):
    answer = 0
    arr = []
    score.sort()
    while len(score) != 0 :
        arr.append(score.pop())
        if len(arr) == m:
            answer += min(arr) * m
            arr = []
    return answer