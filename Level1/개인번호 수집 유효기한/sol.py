def solution(today, terms, privacies):
    answer = []
    today = list(map(int,today.split('.')))
    terms_list = []
    dic_term = {}   #약관
    
    # 약관을 dict형으로 선언
    for t in terms:
        terms_list = t.split()  # split은 list형으로 반환
        dic_term[terms_list[0]] = int(terms_list[1])
    # index오류를 막기 위해서 int값으로 각각 참조하기
    for i in range(len(privacies)):
        # . 기준으로 split해서 day값으로 모두 환산
        i_s = privacies[i].split(' ')
        date_s = list(map(int,i_s[0].split('.')))
        #year
        y = today[0] - date_s[0]
        #month
        m = today[1] - date_s[1]
        #day
        d = today[2] - date_s[2]
        
        t_d = (y*12*28) + (m*28) + d
        k = dic_term.get(i_s[1])
        d_d = 28 * k
        print(t_d, d_d)
        if d_d <= t_d:
            x = i + 1
            answer.append(x)
    
    return answer