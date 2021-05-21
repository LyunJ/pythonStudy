# list copy

# 얕은 복사
scores = [65,70,90,89,78]
value = scores
print(value)

scores[3] = 98
print(value)

# 깊은 복사
value2 = scores.copy()
scores[3] = 89
print(value2)

value3 = list(scores)
scores[0] = 150
print(value3)

import copy
value4 = copy.deepcopy(scores)
scores[2] = 10
print(value4)