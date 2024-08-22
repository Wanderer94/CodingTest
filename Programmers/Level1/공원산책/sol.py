def solution(park, routes):
    answer = []
    # 범위 밖을 "X"로 표시
    park_arr = [["X" for i in range(len(park[0]) + 2)] for j in range(len(park) + 2) ]
    # 2차원 배열로 만들기
    for i in range(len(park)):
        # 시작지점 찾기
        if park[i].find('S') != -1:
            answer = [i + 1, park[i].find('S') + 1]
        park_col = list(park[i])
        for p in range(len(park_col)):
            park_arr [i + 1][p + 1] = park_col[p]
    
    for route in routes:
        answer = move(answer, route, park_arr)
    answer[0] -= 1
    answer[1] -= 1
    return answer

def move(point, route, park):
    direction = route[0]
    length = int(route[-1])
    check_point = point[:]
    check = 0
    for i in range(length):
        if direction == "E":
            point[1] += 1
            check = park[point[0]][point[1]]
        elif direction == "W":
            point[1] -= 1
            check = park[point[0]][point[1]]
        elif direction == "S":
            point[0] += 1
            check = park[point[0]][point[1]]
        elif direction == "N":
            point[0] -= 1
            check = park[point[0]][point[1]]
        if check == "X":
            return check_point
    return point