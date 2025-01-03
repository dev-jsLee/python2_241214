from collections import deque
# 미로찾기를 통한 BFS, DFS 차이 확인하기
# 미로 정의 1은 이동 가능, 0은 이동 불가능(벽)
maze = [
  [1, 0, 1, 0, 0],
  [1, 1, 1, 1, 0],
  [0, 0, 0, 1, 0],
  [1, 1, 1, 1, 1],
  [0, 1, 0, 1, 0]
]

# 너비 우선 탐색을 통한 미로 찾기
def maze_bfs(maze, start, end):
  # start와 end는 두 수로 이루어진 tuple
  # 예) start = (0, 0) end = (4, 3)

  # 미로의 크기 계산
  rows, cols = len(maze), len(maze[0])

  # 큐 초기화: (행, 열, 경로) 튜플을 저장
  # 시작 위치와 빈 경로로 시작
  info = (start[0], start[1], [])
  queue = deque([info])

  # 방문한 위치를 저장하는 집합
  visited = set([start])

  # 위로(-1, 0)
  # 아래로(1, 0)
  # 왼쪽으로(0, -1)
  # 오른쪽으로(0, 1)
  # 방향 정의: 상하좌우
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

  # 큐가 비어있지 않은 동안 반복
  

