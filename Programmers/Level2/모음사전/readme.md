```py
def solution(word):
    answer = 0
    return answer

def DFS_with_adj_list(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited
```

- dfs를 가지고 풀어야한다는 생각까진 접근했는데 어떻게 적용해야할지에 대해서 고민이 되었다
- 다음과 같이 해결하였다.

```py
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
```
