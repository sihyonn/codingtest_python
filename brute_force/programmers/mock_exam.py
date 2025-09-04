

def solution(answers):
    student1 = [1, 2, 3, 4, 5] 
    student2 = [2, 1, 2, 3, 2, 4, 2, 5] 
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] 
    
    scores = [0,0,0]
    
    for i, ans in enumerate(answers):
        if ans == student1[i % len(student1)]:
            scores[0] +=1
        if ans == student2[i % len(student2)]:
            scores[1] += 1
        if ans == student3[i % len(student3)]:
            scores[2] += 1
            
    max_score = max(scores)
    
    return [i+1 for i, score in enumerate(scores) if score == max_score]


# 테스트
answers = [1,2,3,4,5]
print(solution(answers))