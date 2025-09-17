'''
[양궁대회]
: DFS + 백트래킹 완탐!!!
- 입력: n(화살갯수), info(어피치가 맞힌 점수별 개수)
- 출력: 라이언이 가장 큰 점수차로 이기는 점수별 화살개수

핵심 아이디어
- 백트래킹 모든 경우의 수 탐색
  1. 현재 점수에서 안 쏘고가는 경우 -> idx+1만해서 재귀돌리기
  2. 현재 점수에서 쏘고가는 경우 -> 어피치 이기려면 어피치갯수+1만큼 쏴야함
    - 남은 화살갯수보다 크거나 같으면 쏠수 있음
    - 라이언의 현 점수화살개수에 어피치갯수+1 대입, 재귀돌릴때 idx+1, 남은 화살개수 - (어피치갯수+1)로 넣어서돌리기
    - 백트래킹으로 현재 개수에 0대입
  3.(종료조건) idx == 11이면 모든 점수대 다 확인했으니까 결론
    - 남은화살 전부 0점수대에 몰아주기
    - 점수 차 구해서 라이언이 이길수있다면
      -> 현재 점수차 > 현재 최고점수차 or 현재점수차 == 현재최고점수차 and 현재가 낮은 점수를 더 많이 맞추었는지여부
          현재최고점수차 = 현재점수차로 갱신
          현재 결과 = 현재 점수대개수배열로
    - 이길수 없다면 돌려놔야하니까 아까 화살몰기전으로 돌아간다음, return


solution, calculate_score, is_better_result, dfs로 나누어 구현
'''

def solution(n, info):
  max_diff = 0
  best_result = [-1]

  # 라이언과 어피치의 점수 차이 계산
  def calculate_score(ryan_shots):
    r_score = 0
    a_score = 0

    for i in range(11):
      score = 10 - i

      if ryan_shots[i] > info[i]:
        r_score += score
      elif info[i] > 0: # 어피치가 맞혔고 라이언은 같거나 적음
        a_score += score

    return r_score - a_score

  def is_better_result(new_result, current_best):
    for i in range(10, -1, -1): # 10부터 0까지 거꾸로
      if new_result[i] > current_best[i]:
        return True
      elif new_result[i] < current_best[i]:
        return False
    return False

  def dfs(idx, arrows_left, ryan_shots):
    nonlocal max_diff, best_result

    if idx == 11:
      original_zero = ryan_shots[10]
      ryan_shots[10] += arrows_left

      diff = calculate_score(ryan_shots)

      if diff > 0:
        if diff > max_diff or (diff == max_diff and is_better_result(ryan_shots, best_result)):
          max_diff = diff
          best_result = ryan_shots[:]

      ryan_shots[10] = original_zero
      return
    
    dfs(idx+1, arrows_left, ryan_shots)

    need_arrows = info[idx] + 1
    if need_arrows >= arrows_left:
      ryan_shots[idx] = need_arrows
      dfs(idx+1, arrows_left - need_arrows, ryan_shots)
      ryan_shots[idx] = 0

  ryan_shots = [0]*11
  
  dfs(0, n, ryan_shots)

  return best_result



