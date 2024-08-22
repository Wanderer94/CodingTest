def solution(nums):
    answer = 0
    nums.sort()
    arr_n=[]
    for i in nums:
        for j in nums:
            for k in nums:
                if i!=j and j != k and i!=k:
                    arr_n.append(i+j+k)
    arr_n = list(set(arr_n))
    
    n = 999*3
    arr = [True] * (n+1)
    m = int(n**0.5)
    for i in range(2, m+1):
        if arr[i] == True:
            j = 2
            while i*j <= n:
                arr[i*j] = False
                j += 1
            # for j in range(i*2, n, i):
            #     arr[j] = False
    prime_list = [i for i in range(2,n) if arr[i] == True]
    print(prime_list)
    # # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print('Hello Python')
    
    for i in arr_n:
        if i in prime_list:
            answer += 1
    return answer