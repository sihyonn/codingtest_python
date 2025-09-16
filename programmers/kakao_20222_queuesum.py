from collections import deque

'''
[두 큐 합 같게 만들기]
1. 절대 같을 수 없는 케이스 => 총합 홀수일때 return -1
2. while문 무한루프 방지 => max_operations 설정
3. count < max_operations 조건에서 반복
  - if queue1의 합 == 총합의 절반이면 return count
  - 그리디전략(큰쪽에서 작은쪽으로)
    => queue1의 합 > 총합 절반이면 queue1에서 popleft()하고 queue2에 append, 각 큐의 sum에서 증감해주기
    => queue2의 합 > 총합 절반인거면 반대로
    * 각각의 경우에서 큐 비어있는지 확인 후 비었으면 return -1 선행
  - count + 1
'''



def solution(queue1, queue2):
  q1 = deque(queue1)
  q2 = deque(queue2)

  sum1 = sum(q1)
  sum2 = sum(q2)
  total = sum1 + sum2

  if total % 2 != 0:
    return -1
  
  target = total // 2
  count = 0
  max_operations = len(queue1) * 3

  while count < max_operations:
    if sum1 == target:
      return count
    
    if sum1 > target:
      if not q1: return -1
      el = q1.popleft()
      q2.append(el)
      sum1 -= el
      sum2 += el
    else:
      if not q2: return -1
      el = q2.popleft()
      q1.append(el)
      sum1 += el
      sum2 -= el
    
    count += 1

  return -1


print(solution([1, 2, 1, 2], [1, 10, 1, 2]))