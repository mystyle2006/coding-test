"""
1. 아이디어
- 1부터 N 중에 하나를 선택한 뒤
- 다음 1부터 N까지 선택할 때 이미 선택한 값이 아닌 경우 선택
- M개가 되었을 때 출력

2. 시간복잡도
- 중복이 불가, N!

3. 자료구조
- 결과값: int[]
- 방문: bool[]
"""

import sys

input = sys.stdin.readline
n, m = map(int, input().split())

rs = []
chk = [False] * (n + 1)


def recur(depth):
    if depth == m:
        print(" ".join(map(str, rs)))
        return

    for i in range(1, n + 1):
        if chk[i] is False:
            chk[i] = True
            rs.append(i)
            recur(depth + 1)
            chk[i] = False
            rs.pop()


recur(0)
