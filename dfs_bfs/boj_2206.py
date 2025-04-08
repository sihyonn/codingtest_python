from collections import deque
'''
백준 #2206 - 벽 부수고 이동하기

[필요한 것]
1. n, m 입력받기
2. graph 입력받기
3. 방문여부 배열(3차원 [x][y][wall])
4. 최단거리 = bfs
  : 큐 사용 -> 상태정보포함 x, y, 벽부순회수, 거리 
  - 큐 생성 및 초기화 -> 0, 0, 0, 1
  - 현재 방문처리
  - 큐 빌때까지
    - 큐에서 하나 빼서
    - 목적지 도착했다면 거리 반환 (if)
    - 아직 목적지 도착안했다면 상하좌우돌기(elif)
      - 다음 좌표 구하고
      - 범위 안벗어나면
        1. 이동할 수 있고, 방문안했다면 => 방문처리 / 큐에 다음좌표, 벽부순횟수, 거리+1 추가
        2. 이동할 수 없고, 벽부술횟수남아있고, 벽을 부수고 방문한게아니면 => 벽부순방문처리 / 큐에 다음좌표, 부순횟수+1, 거리+1 추가
    - 불가능이면 -1(else)
'''

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]


def bfs(x, y):
  q = deque()
  q.append((x, y, 0, 1))
  visited[x][y][0] = True

  while q:
    x, y, w, d = q.popleft()

    if x == n - 1 and y == m - 1:
      return d

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      nx, ny = x + dx, y + dy

      if 0 <= nx < n and 0 <= ny < m:
        if graph[nx][ny] == 0 and not visited[nx][ny][w]:
          visited[nx][ny][w] = True
          q.append((nx, ny, w, d + 1))

        elif graph[nx][ny] == 1 and w == 0 and not visited[nx][ny][1]:
          visited[nx][ny][1] = True
          q.append((nx, ny, w + 1, d + 1))

  return -1


print(bfs(0, 0))
