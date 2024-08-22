```py
def solution(numbers, target):
    answer = 0
    return answer

def bfs

def dfs
```

- 2가지 방법 모두 풀어보려했지만 암기가 필요하다고 다시 한번 느꼈다.
- 구현 방식에 대해서 암기가 필요하다!
- 큐를 어떻게 쓸지, 스택을 어떻게 사용할지에 대해서 암기가 필요!

```py
def solution(numbers, target):
  leaves = [0]          # 모든 계산 결과를 담자
  count = 0

  for num in numbers :
    temp = []

    # 자손 노드
    for leaf in leaves :
      temp.append(leaf + num)    # 더하는 경우
      temp.append(leaf - num)    # 빼는 경우

    leaves = temp

  # 모든 경우의 수 계산 후 target과 같은지 확인
  for leaf in leaves :
    if leaf == target :
      count += 1

  return count
```

- BFS를 사용해서 풀었지만, 너무 어렵게 생각하고 있었다.
- 스택으로 생각해보면 모든 경우의 수를 하나씩 차례로 진행해보면 되는 것.
- DFS로 풀어보자!

```py
def dfs(numbers, target, idx, values):     # idx : 깊이 / values : 더하고 뺄 특정 leaf 값

    global cnt
    cnt = 0

    # 깊이가 끝까지 닿았으면
    if idx == len(numbers) & values == target :
    	cnt += 1
        return

    # 끝까지 탐색했는데 sum이 target과 다르다면 그냥 넘어간다
    elif idx == len(numbers) :
    	return

    # 재귀함수로 구현
    dfs(numbers, target, idx+1, values + numbers[idx])   # 새로운 value 값 세팅
    dfs(numbers, target, idx+1, values - numbers[idx])

 def solution(numbers, target) :

    global cnt
    dfs(numbers, target, 0, 0)

    return cnt
```

- 암기해야할 부분이 해당 내용이라고 생각된다.
- bfs와 dfs의 차이점에 대해서 공부해볼필요가 있다.
- 최단의 하나의 경우는dfs를 사용하는 것이 더 효율 적일 것이고, 모든 경우를 다 탐색하고 싶다면 bfs를 사용하는 것이 좋을 것 같다.
