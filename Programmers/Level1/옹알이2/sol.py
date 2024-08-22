def solution(babbling):
    answer = 0
    l = [ "aya", "ye", "woo", "ma" ]
    for i in babbling:
        ans = ''
        result = False
        index = -1
        for j in i:
            ans += j
            if ans == "aya" and index != 0:
                index = l.index(ans)
                ans = ''
                result = True
            elif ans == "ye" and index != 1:
                index = l.index(ans)
                ans = ''                
                result = True
            elif ans == "woo" and index != 2:
                index = l.index(ans)
                ans = ''
                result = True
            elif ans == "ma" and index != 3:
                index = l.index(ans)
                ans = ''
                result = True
            else:
                result = False
        if result == True:
            answer += 1
                    
    
    return answer