def solution(number, limit, power):
    answer = 1
    for i in range(2, number+1 ):
        count = 0
        for j in range(1 , int(i**(1/2))+1): #제곱근 활용!
            if i % j == 0:
                if j == i//j:
                    count += 1
                else:
                    count += 2
            print(count)
            if count > limit:
                count = power
                break
        answer += count
    return answer