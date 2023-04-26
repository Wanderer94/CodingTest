def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        ans = ''
        a = format(arr1[i],'b')
        a = list('0'*(n-len(a)) + a)
        b = format(arr2[i],'b')
        b = list('0'*(n-len(b)) + b)
        for j in range(n):
            if a[j] == b[j] == '0':
                a[j] = ' '
            else:
                a[j] = '#'
            ans += a[j]
        answer.append(ans)   
    return answer