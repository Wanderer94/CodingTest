def solution(new_id):
    answer = ''
    #1단계
    new_id = new_id.lower()
    #2단계
    list_id = list(new_id)
    check2 = []    
    for i in list_id:
        if i.isalnum():
            check2.append(i)
            continue
        elif i == '-' :
            check2.append(i)
            continue
        elif i == '_' :
            check2.append(i)
            continue
        elif i == '.':
            check2.append(i)
            continue
    list_id = check2
    #3단계
    check3 = []
    for i in list_id:
        if len(check3) == 0:
            check3.append(i)
        elif i == '.' and check3[-1] == '.':
            continue
        else:
            check3.append(i)
    list_id = check3
    #4단계
    if list_id[0] == '.':
        list_id.remove('.')
    if len(list_id) != 0 and list_id[-1] == '.':
        list_id.pop()
    print(list_id)
    #5단계
    if len(list_id) == 0:
        list_id.append('a')
    #6단계
    if len(list_id) >= 16:
        list_id = list_id[0:15]
        if list_id[-1] == '.':
            list_id.pop()

    #7단계
    if len(list_id) <= 2:
        while len(list_id) != 3:
            list_id.append(list_id[-1])
    
    #결과 리턴
    for i in list_id:
        answer += i
    return answer