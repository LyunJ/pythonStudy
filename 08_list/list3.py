# remove(x) : 가장 첫번째 만나는 값을 삭제

# n = [1, 2, 3, 4, 5, 6, 7, 1]
# n.remove(1)
# print(n)
# cnt = n.count(1)
# print(cnt)

# pop() : 마지막 값을 꺼내서 반환함 pop(index) : index 위치의 값을 꺼내서 반환
# data = n.pop()
# print(n)
# print(data)
#
# data = n.pop(0)
# print(data)

# 2차원 리스트 연습문제
# 10명의 학생의 국어, 영어, 수학 점수가 2차원 리스트 형식으로 저장된 경우

STUDENT = 10
score_table = [

]

import random as rd

for i in range(STUDENT):
    score_table.append([rd.randint(0, 101), rd.randint(0, 101), rd.randint(0, 101)])

for i in range(STUDENT):
    print(f'{score_table[i]},{sum(score_table[i])},{sum(score_table[i]) / len(score_table[i]):.2f}')
    print('{},{},{:.2f}'.format(score_table[i], sum(score_table[i]), sum(score_table[i]) / len(score_table[i])))
