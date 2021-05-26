# enumerate(iterable,start=0)
# 시퀀스(리스트,튜플,문자열,range)를 인덱스값을 포함하는 enumerate 객체로 반환
# 반복문 사용 시 몇 번째 반복문인지 확인이 필요할 수 있습니다. 이때 사용합니다.
# 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환합니다


# iterator
enum = enumerate(['apple', 'banana', 'melon'])
print(enum)
while True:
    try:
        e = next(enum)
    except StopIteration:
        break
    print(e)

# iterable
list1 = ['apple', 'banana', 'melon']
list1_iter = list1.__iter__()
while True:
    try:
        l = next(list1_iter)
    except StopIteration:
        break
    print(l)

# range()
print(range(4))
print(list(range(5)))
print(tuple(range(4)))

# zip(*iterable) : 각 iterable에서 동일한 인덱스 요소를 추출하여 묶어서 반환
print(zip([1,3,5],['cat','dog','horse'])) # 구조 변환을 해주어야함
print(list(zip([1,3,5],['cat','dog','horse'])))
print(dict(zip([1,3,5],['cat','dog','horse'])))
print(tuple(zip([1,3,5],['cat','dog','horse'])))

# map()
print(list(map(str,range(10))))
print(tuple(map(str,range(10))))
print(set(map(str,range(10))))
