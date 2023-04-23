def solution(s):
    answer = True
    p = s.count('p') + s.count('P')
    y = s.count('y') + s.count('Y')
    if p != y:
        answer = False
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer

#lower 함수에 대해서 