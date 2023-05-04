def solution(s, n):
    answer = ''
    # print(ord('a')- ord('z') )
    for i in s:
        #알파벳인지 확인
        if i.isalpha():
            # 대문자 소문자 구분
            if i.isupper():
                if ord('Z') < ord(i) + n:
                    a = (ord(i) + n) - 26
                    answer += chr(a)
                else:
                    answer += chr(ord(i) + n)
                    
            elif i.islower():
                if ord('z') < ord(i) + n:
                    a = (ord(i) + n) - 26
                    answer += chr(a)
                else:
                    answer += chr(ord(i) + n)
        else:
            answer += i
    print(answer)
    return answer