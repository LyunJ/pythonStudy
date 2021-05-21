# sort() reverse() sorted()

# #리스트를 정렬
# a = [3,6,0,-4,1]
# a.sort()
# print(a)
# a.reverse()
# print(a)
# # 정렬 후 새로운 리스트를 반환
# new_a = sorted(a,reverse=True)
# print(new_a)

# string = ['Apple','Banana','melon','apple']
# string.sort()
# print(string)
# # 대소문자 구분 없이 정렬
# string.sort(key=str.upper)
# print(string)

# index(n) 메소드 : n의 위치 반환 없으면 에러
a = [3,6,0,-4,1]
b = a.index(6)
print(b)