def solution(brown, yellow):
    
    # 1. 약수 구하기. 세로는 약수가 될 수 있음
    candidates = []
    
    for h in range(1, yellow + 1):
        if yellow % h == 0:
            w = yellow // h
            if w >= h:
                candidates.append((w, h))
    
    # 2. 브라운 블록 조건 확인
    for w, h in candidates:
        if (w + 2) * (h + 2) - yellow == brown:
            return [w + 2, h + 2]


'''
1. 노랑블록개수 기준 가로, 세로 조합찾기(가로 >=세로)
2. 브라운블록 개수와 일치여부 확인
    브라운블록 = 전체블록 - 노랑블록
    brown = (가로 * 2) + (세로 * 2) - yellow
3. 계산한 브라운 블록수와 입력값 일치하면 [가로+2, 세로+2] 반환

'''