from collections import deque

def solution(maps):
    N = len(maps[0])
    M = len(maps)
    case = []
    if N == 1 and M == 1:  # n과 m이 모두 1인 경우
        return -1 if maps[0][0] == 0 else 0
    def bfs():
        q = deque([(0, 0, 1)])  # (x, y, count)
        visited = [[False for _ in range(N)] for __ in range(M)]
        visited[0][0] = True

        while q:
            x, y, cnt = q.popleft()

            if x == M - 1  and y == N - 1:  # 상대 팀 진영에 도착하면 count 반환
                return cnt

            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # 상우하좌 이동
                nx = x + dx
                ny = y + dy
                if 0 <= nx < M and 0 <= ny < N and maps[nx][ny] == 1 and not visited[nx][ny]:
                    q.append((nx, ny, cnt + 1))
                    visited[nx][ny] = True
        return -1
    return bfs()