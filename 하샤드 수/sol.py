def solution(x):
    answer = True
    x_s = 0
    print(sum(int(x) for i in str(x)))
    int(x) for i in str(x)
    for i in str(x):
        x_s += int(i)
    print(x_s)
    if x % x_s == 0:
        return  True
    return False
    # return x % sum(int(x) for x in str(x)) == 0