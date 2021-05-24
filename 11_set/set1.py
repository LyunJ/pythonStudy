s1 = set()
print(type(s1))
s1 = {3, 5, 7, 1, 3, 4}
print(s1)

# list는 set에 넣을 수 없음
# 변경 불가한 tuple만 가능
# s2 = {[10,20]}
s2 = {(10, 20)}
print(s2)

# 인덱스 사용 불가
# s1[0]

# 데이터 추가 .add
s2.add(90)
print(s2)

s1.add(-9)
print(s1)

# 데이터 삭제 .remove()
s1.remove(-9)
print(s1)
# s1.remove(0) # 존재하지 않으면 에러 발생
s1.discard(0) # 에러 발생 X
print(s1)

s1.clear()
print(s1)

del s1
# print(s1)

s1 = {3,4,1,6}
s2 = {2,4,5,8,3}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)