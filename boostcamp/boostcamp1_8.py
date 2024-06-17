from hmac import new


def encode(N, S, K):
    S = list(S)
    new_str = ''
    for i in S :
        i = int(i) + K
        if i > 10:
            new_str += str(i)[-1]
        else:
            new_str += str(i)
    return new_str

def sol(N, S):
    arr = [] * 9
    for i in range(9):
        arr.append(encode(N,S,i))