'''
백준 #2606 - 바이러스

[필요한 것]
1. 전체 컴퓨터 수 받기
2. 방문여부 배열
3. 인접그래프
4. dfs
  - 시작번호를 인자로 받음
  - 현재 번호 방문처리
  - graph[현재번호] 원소 돌면서 방문안했으면 카운트 1증가, dfs(방문안한 원소)로 재귀
  - return count
'''

# 전체 컴퓨터 수 받기
n = int(input())
m = int(input())
visited = [False] * (m + 1)

# 입력값으로 인접그래프 만들기
graph = [[] for _ in range(n+1)]  # 1.이중배열로 초기화
for _ in range(m):                # 2.입력값받아 양방향 그래프 채워주기
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)



def dfs(x):
  visited[x] = True
  count = 0

  for i in graph[x]:
    if not visited[i]:
       count += dfs(i) + 1    # count도 단순 1증가 아닌 재귀적으로
      
  return count
  

print(dfs(1))