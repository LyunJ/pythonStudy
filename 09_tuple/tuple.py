# tuple 생성 : tuple() or ()

# t1 = (1, 2)
# print(t1)
# t2 = 1, 3, 4
# print(t2)
# t3 = t1, (5, 6, 7)
# print(t3)
# t4 = [1, 4], [5, 6]
# print(t4)
# t5 = tuple([1, 4])
# print(t5)

# 요소 변경 불가
# print(t1[2])
# t1[2] = 10

# 요소 추가 불가
# t1.append(-9)
# 요소 삭제 불가
# del(t1[2])

# 튜플 자체 삭제는 가능
# del(t1)

# tuple.index(), .count()

# tt = 'a', 'b', 'c', 'e', 'a', 'd'
# e의 위치 반환
# i = tt.index('e')
# print(i)
# b의 개수 반환
# c = tt.count('b')
# print(c)

# slicing
# t = tt[:]
# t = tt[1:5]
# print(t)

# +,* 연산
# 기존의 튜플로 새로운 튜플 생성은 가능
# print(t1 + t2)
# print(tt * 2)


# tt = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
#
# for t in tt:
#     for a in t:
#         print(a,end=' ')
#     print()

myTuple = (10, 20, 30)
# 리스트로 변환 가능
list(myTuple)
print(myTuple + tuple([40]))
myTuple = myTuple + tuple([40])
print(myTuple)


