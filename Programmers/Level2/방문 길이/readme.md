```py
def solution(dirs):
    answer = 1
    table = [[0]*10 for _ in range(10)]
    point = [5,5]
    for d in dirs:
        point = move(point,d)
        if table[point[0]][point[1]] == 0:
            table[point[0]][point[1]] = 1
            answer += 1
    return answer

def move(point, d):
    if d == "U":
        if point[1]+1 < 10:
            point[1] += 1
    elif d == "D":
        if point[1]-1 > 0:
            point[1] -= 1
    elif d == "R":
        if point[0]+1 <10:
            point[0] += 1
    elif d== "L":
        if point[0]-1 > 0:
            point[0] -= 1
    return point
```

- 다음과 같이 두개의 함수로 나누어서 이차원 배열로 생각해 진행했다.
- 하지만 굳이 0이 많아지는 배열을 사용할 필요가 없다고 생각이 들었다.
- 중복할 필요가 없다는 점을 위주로 생각해보면 set을 사용하는게 도움이 될 것으로 판단된다.

```py
def solution(dirs):
    x,y = 0,0
    sets = set()
    direction = {'U': (1, 0), 'D': (-1, 0), 'R': (0, 1), 'L': (0, -1)}
    for d in dirs:
        dy, dx = direction[d]
        nx = x+dx
        ny = y+dy
        if -5 <= ny <= 5 and -5 <= nx <= 5:
            sets.add(((y, x), (ny, nx)))
            sets.add(((ny, nx), (y, x)))
            y = ny
            x = nx
    return len(sets) // 2
```
