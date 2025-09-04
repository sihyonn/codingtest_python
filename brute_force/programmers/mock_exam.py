

def solution(answers):
    students = [[1, 2, 3, 4, 5],[2, 1, 2, 3, 2, 4, 2, 5],[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]] 
    scores = [0,0,0]
    
    for i, ans in enumerate(answers):
        for j, student in enumerate(students):
          if ans == student[i % len(student)]:
             scores[j] += 1
    
    return [i+1 for i, student in enumerate(scores) if student == max(scores)]


# 테스트
answers = [1,2,3,4,5]
print(solution(answers))