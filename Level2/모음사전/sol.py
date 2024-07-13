answer = 0
def DFS(string,word) :
    alphabets = ['A','E','I','O','U']
    global answer
    answer += 1

    if ( string == word ):
        return True

    if ( len(string) == 5) :
        return False

    for a in alphabets :
        if (DFS(string + a,word) == True) :
            return True

def solution(word):
    global answer
    alphabets = ['A','E','I','O','U']

    for a in alphabets :
        if (DFS(a,word) == True) :
            return answer