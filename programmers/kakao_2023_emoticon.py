'''
1. 문제이해
  - 이모티콘마다 할인율 10, 20, 30, 40%에서 정할 수 있음
  - 사용자별로 구매기준할인율 있음 이 이상될때만 구매
  - 할인들어간 이모티콘 가격 총합이 기준가격 이상이면 플러스 가입

=> 완탐 + 백트래킹

2. 아이디어
  - 할인율 조합 생성 10, 20, 30, 40을 가지고 => 4^n가지 조합
  - 각 조합마다
    1. 이모티콘별 할인된 금액 계산
    2. 사용자별로 본인 기준에 맞는 이모티콘만 골라서 금액 합산
    3. 합산액 >= 기준액이면 플러스+1, 아니면 금액그대로 매출에 더함
    (플러스가입자, 총 이모티콘 매출은 조합 내 전역)
3. 결과 갱신
  한 조합이 끝나고 이전과 현재를 비교해서
  플러스 가입자수가 더 많으면 무조건 갱신
  플러스 가입자수 같으면 금액비교해서 높은걸로 갱신
'''








# 할인율 조합 생성 함수
# - 조합 완성됐으면(idx === emoticons.length) 시뮬레이션 돌리기
# - 아니면 할인율 배열 돌면서 조합배열[idx]에 할인율 대입하고, idx+1해서 생성함수 재귀
  
# 시뮬레이션
# - 완성된 조합배열 받아서 유저배열 도는데 이모티콘 길이만큼 돌면서 할인율이 유저기준비율 이상이면 할인금액 계산해서 유저별 total 비용에 더하기
# - 총 유저별 토탈비용이 기준액 이상이면 가입자수 1증가, 아니면 매출 + 토탈비용
# 이 한 조합에대해 구해진 총 유저에 대한 플러스가입자수, 금액이 나왔으니 최적 결과 갱신  
  

DISCOUNT_RATES = [10, 20, 30, 40]

def generate_combinations(emoticon_count):
 
    results = []
    cur_combination = [0] * emoticon_count
    
    def backtrack(idx):
        if idx == emoticon_count:
            results.append(cur_combination[:])
            return
        
        for rate in DISCOUNT_RATES:
            cur_combination[idx] = rate
            backtrack(idx + 1)
    
    backtrack(0)
    return results

def simulate_purchase(users, emoticons, discounts):
   
    plus_users = 0
    total_amount = 0
    
    for standard_rate, standard_amount in users:
        user_total_price = 0
        
        for i in range(len(emoticons)):
            if discounts[i] >= standard_rate:
                discount_price = emoticons[i] * (100 - discounts[i]) // 100
                user_total_price += discount_price
        
        if user_total_price >= standard_amount:
            plus_users += 1
        else:
            total_amount += user_total_price
    
    return plus_users, total_amount

def solution(users, emoticons):

    all_combinations = generate_combinations(len(emoticons))
    max_plus_users = 0
    max_total_amount = 0
    
    for discounts in all_combinations:
        plus_users, total_amount = simulate_purchase(users, emoticons, discounts)
        
        if (plus_users > max_plus_users or 
            (plus_users == max_plus_users and total_amount > max_total_amount)):
            max_plus_users = plus_users
            max_total_amount = total_amount
    
    return [max_plus_users, max_total_amount]

# 테스트
if __name__ == "__main__":
    users = [[40, 10000], [25, 10000]]
    emoticons = [7000, 9000]
    print(solution(users, emoticons))  # [1, 5400]