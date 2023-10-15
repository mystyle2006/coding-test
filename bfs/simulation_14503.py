"""
1. 아이디어
- 현재 위치가 청소되어 있지 않으면 바로 청소한다.
- 주변에 청소되지 않은 빈칸이 있으면 현재 바라보는 위치 d를 기준으로 4번 반복하여 전진한다.
- 주변에 청소되지 않은 빈칸이 없으면 현재 바라보는 위치 d를 기준으로 후진한다.
- 위 조건에 만족되지 않으면 종료한다.
2. 시간복잡도
- M*N*4 = 50^2*4 = 1만
3. 자료구조
- map
- d: 청소기가 바라보는 방향 (0: 북(0, -1), 1: 동(1, 0), 2: 남(0, 1), 3:서(-1, 0))

- r,c: 현재 청소기의 위치
- cnt: 청소 영역 수
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
UNCLEAN_ROOM = 0
CLEAN_ROOM = 2
WALL = 1

sw = False

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

while True:
    if map[r][c] == UNCLEAN_ROOM:
        map[r][c] = CLEAN_ROOM
        cnt += 1

    sw = False
    for i in range(1, 5):
        # 바라보는 방향에서 반시계 반향으로
        ny = r + dy[d - i]
        nx = c + dx[d - i]
        if 0 <= ny < n and 0 <= nx < m:
            if map[ny][nx] == UNCLEAN_ROOM:
                # -5 가 나올 수 있으므로 최대 범위 -4 ~ 3 에서 벗어나지 않도록 처리
                d = (d - i + 4) % 4
                r = ny
                c = nx
                sw = True
                break

    if sw is False:
        # 바라보는 방향에서 후진
        ny = r - dy[d]
        nx = c - dx[d]
        if 0 <= ny < n and 0 <= nx < m:
            if map[ny][nx] == WALL:
                break
            else:
                r = ny
                c = nx

print(cnt)
