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
