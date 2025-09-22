'''
[택배 배달과 수거하기]
: 남은일의 양 = 누적처리가 핵심!
- 먼집부터(역순) 처리, 왕복이니까 한 번 가면 돌아올때까지 거리 * 2배
- 각 위치에서 그 위치까지의 모든 배달, 수거 요청 누적

'''
def solution(cap, n, deliveries, pickups):
    answer = 0
    d_remain = 0 
    p_remain = 0  
    
    # 가장 먼 집부터 처리 (n-1부터 0까지)
    for i in range(n - 1, -1, -1):
        d_remain += deliveries[i]
        p_remain += pickups[i]
        
        # 현재 위치에서 배달이나 수거가 필요한 경우
        while d_remain > 0 or p_remain > 0:
            # 트럭이 현재 집까지 왕복해야 함
            answer += (i + 1) * 2
            
            # 트럭 용량만큼 배달하고 수거
            d_remain -= cap
            p_remain -= cap
    
    return answer
