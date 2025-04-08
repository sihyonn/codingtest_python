N = int(input())
regions = [list(map(int, input().split())) for _ in range(N)]
max_height = max(map(max, regions))
max_safe_area = 0


def dfs(x, y, h, visited):
  visited[x][y] = True

  for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    nx, ny = x + dx, y + dy

    if 0 <= nx < N and 0 <= ny < N:
      if not visited[nx][ny] and regions[nx][ny] > h:
          dfs(nx, ny, h, visited)


for h in range(0, max_height + 1):
  visited = [[False] * N for _ in range(N)]
  count = 0

  for i in range(N):
    for j in range(N):
      if not visited[i][j] and regions[i][j] > h:
        dfs(i, j, h, visited)
        count += 1

  max_safe_area = max(max_safe_area, count)

print(max_safe_area)
